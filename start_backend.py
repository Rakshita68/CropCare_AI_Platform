import uvicorn
import os
import sys

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

if __name__ == "__main__":
    # Set environment variables for local development
    os.environ.setdefault('MODEL_DIR', './backend/ml/models')
    
    # Start the FastAPI server
    uvicorn.run(
        "backend.app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )