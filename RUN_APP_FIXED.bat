@echo off
title FitPulse AI Assistant Fixed
cd /d "%~dp0"

echo ==============================================
echo FitPulse AI Assistant Fixed
echo ==============================================
echo Closing old Streamlit is recommended before running.
echo.

echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Starting app on 127.0.0.1:8510 ...
start "" "http://127.0.0.1:8510"
python app.py

pause
