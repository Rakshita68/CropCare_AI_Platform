import subprocess
import sys
import os
import time
from threading import Thread

def run_backend():
    """Run the FastAPI backend server"""
    print("Starting backend server...")
    subprocess.run([sys.executable, "start_backend.py"])

def run_frontend():
    """Run the frontend HTTP server"""
    print("Starting frontend server...")
    time.sleep(2)  # Wait for backend to start
    subprocess.run([sys.executable, "start_frontend.py"])

def init_database():
    """Initialize the database"""
    print("Initializing database...")
    subprocess.run([sys.executable, "init_database.py"])

if __name__ == "__main__":
    print("=== Agriculture AI System Startup ===")
    
    # Change to project directory
    os.chdir(os.path.dirname(__file__))
    
    # Initialize database
    init_database()
    
    print("\nStarting servers...")
    print("Backend will run on: http://localhost:8000")
    print("Frontend will run on: http://localhost:3000")
    print("\nPress Ctrl+C to stop all servers\n")
    
    # Start backend in a separate thread
    backend_thread = Thread(target=run_backend, daemon=True)
    backend_thread.start()
    
    # Start frontend (this will block)
    try:
        run_frontend()
    except KeyboardInterrupt:
        print("\nShutting down all servers...")
        sys.exit(0)