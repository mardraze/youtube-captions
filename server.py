from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

app = Flask(__name__)


@app.get("/api/transcript")
def get_transcript():
    """
    Przykład użycia:
    GET /api/transcript?video_id=dQw4w9WgXcQ
    GET /api/transcript?video_id=dQw4w9WgXcQ&languages=pl,en
    """
    video_id = request.args.get("video_id")
    if not video_id:
        return jsonify({"error": "Brak parametru 'video_id'"}), 400

    languages_param = request.args.get("languages", "pl,en")
    languages = [lang.strip() for lang in languages_param.split(",") if lang.strip()]

    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=languages)
        data = transcript.to_raw_data()

        return jsonify({
            "video_id": video_id,
            "language": transcript.language,
            "language_code": transcript.language_code,
            "is_generated": transcript.is_generated,
            "transcript": data,
        })

    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable, CouldNotRetrieveTranscript) as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Nieoczekiwany błąd: {e}"}), 500


@app.get("/")
def index():
    return jsonify({
        "message": "YouTube Transcript API",
        "usage": "/api/transcript?video_id=<ID>&languages=pl,en",
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
