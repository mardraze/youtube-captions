# Skrypt uruchamiajacy serwer w PowerShell (Windows)

# Przejdz do katalogu, w ktorym znajduje sie ten skrypt
Set-Location -Path $PSScriptRoot

$VenvDir = ".venv"

# Utworz wirtualne srodowisko, jesli jeszcze nie istnieje
if (-not (Test-Path $VenvDir)) {
    Write-Host "Tworze wirtualne srodowisko w $VenvDir..."
    python -m venv $VenvDir
}

# Aktywuj wirtualne srodowisko
$ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
& $ActivateScript

# Zainstaluj/zaktualizuj zaleznosci
Write-Host "Instaluje zaleznosci z requirements.txt..."
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt -q

# Uruchom serwer
Write-Host "Uruchamiam serwer..."
python server.py
