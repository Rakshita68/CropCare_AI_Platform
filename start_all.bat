@echo off
start "Backend" cmd /k "cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload"
timeout /t 2 /nobreak > nul
start "Frontend" cmd /k "python start_frontend.py"
timeout /t 3 /nobreak > nul
start http://localhost:3001