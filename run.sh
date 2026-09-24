#!/usr/bin/env bash
set -e

# Przejdź do katalogu, w którym znajduje się ten skrypt
cd "$(dirname "$0")"

VENV_DIR=".venv"

# Utwórz wirtualne środowisko, jeśli jeszcze nie istnieje
if [ ! -d "$VENV_DIR" ]; then
    echo "Tworzę wirtualne środowisko w $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
fi

# Aktywuj wirtualne środowisko
source "$VENV_DIR/bin/activate"

# Zainstaluj/zaktualizuj zależności
echo "Instaluję zależności z requirements.txt..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Uruchom serwer
echo "Uruchamiam serwer..."
python server.py
