@echo off
echo Starting Agriculture AI System...
echo.

echo Initializing database...
python init_database.py
echo.

echo Starting backend server on port 8000...
start "Backend Server" cmd /k "python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload"

echo Waiting for backend to start...
timeout /t 3 /nobreak > nul

echo Starting frontend server on port 3000...
start "Frontend Server" cmd /k "python start_frontend.py"

echo.
echo ================================
echo Agriculture AI System is running!
echo ================================
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to open the application...
pause > nul

start http://localhost:3000