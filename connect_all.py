import subprocess
import sys
import os
import time
import webbrowser

def start_backend():
    print("Starting Backend Server...")
    os.chdir("backend")
    backend_process = subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "app.main:app", "--host", "127.0.0.1", "--port", "8001", "--reload"
    ])
    os.chdir("..")
    return backend_process

def start_frontend():
    print("Starting Frontend Server...")
    frontend_process = subprocess.Popen([sys.executable, "start_frontend.py"])
    return frontend_process

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    
    print("=== Agriculture AI System ===")
    print("Database: Already initialized")
    
    # Start backend
    backend = start_backend()
    time.sleep(3)
    
    # Start frontend  
    frontend = start_frontend()
    time.sleep(2)
    
    print("\nAll services connected!")
    print("Backend API: http://localhost:8001")
    print("Frontend UI: http://localhost:3001")
    print("API Docs: http://localhost:8001/docs")
    
    # Open browser
    webbrowser.open("http://localhost:3001")
    
    try:
        backend.wait()
    except KeyboardInterrupt:
        print("\nShutting down...")
        backend.terminate()
        frontend.terminate()