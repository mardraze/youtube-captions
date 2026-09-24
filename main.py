import json

from youtube_transcript_api import YouTubeTranscriptApi

# VIDEO_ID to fragment z URL, np. z youtube.com/watch?v=dQw4w9WgXcQ
video_id = "dQw4w9WgXcQ"

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id, languages=["pl", "en"])

# to_raw_data() zwraca listę słowników {'text', 'start', 'duration'}
data = transcript.to_raw_data()

print(json.dumps(data, ensure_ascii=False, indent=2))
