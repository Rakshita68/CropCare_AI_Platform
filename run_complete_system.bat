@echo off
echo Starting Global Agriculture AI Platform...
echo.

REM Start backend server in new window
echo Starting Backend Server...
start "Agriculture Backend" cmd /k "cd /d "%~dp0" && python start_server.py"

REM Wait 3 seconds for backend to start
timeout /t 3 /nobreak >nul

REM Open auto-start page that connects to backend
echo Opening Frontend with Backend Connection...
start "" "%~dp0frontend\start_with_backend.html"

echo.
echo ========================================
echo  Global Agriculture AI Platform Started
echo ========================================
echo.
echo Frontend: file:///%~dp0frontend/index.html
echo Backend:  http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to close this window...
pause >nul