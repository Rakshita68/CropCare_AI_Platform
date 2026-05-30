#!/usr/bin/env python3
"""
Setup script to configure API keys for the Agriculture AI Platform
"""
import os

def setup_gemini_api():
    """Setup Gemini API key"""
    print("🔑 Setting up Gemini AI API Key...")
    
    # You can get a free API key from: https://makersuite.google.com/app/apikey
    api_key = "AIzaSyBqJ8K9X2mF4nP7vL3wR5tY8uI6oE1qA9s"
    
    env_path = os.path.join(os.path.dirname(__file__), 'backend', '.env')
    
    with open(env_path, 'w') as f:
        f.write(f"GEMINI_API_KEY={api_key}\n")
    
    print(f"✅ API key configured in: {env_path}")
    print("🤖 Gemini AI is now ready for agriculture assistance!")
    
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    
    try:
        import subprocess
        subprocess.run(["pip", "install", "google-generativeai"], check=True)
        print("✅ Google Generative AI package installed")
        return True
    except Exception as e:
        print(f"⚠️ Could not install packages: {e}")
        print("Please run: pip install google-generativeai")
        return False

if __name__ == "__main__":
    print("🌍 Global Agriculture AI Platform - API Setup")
    print("=" * 50)
    
    # Setup API key
    setup_gemini_api()
    
    # Install requirements
    install_requirements()
    
    print("\n🚀 Setup complete! You can now run:")
    print("   python start_server.py")
    print("\n📋 API Documentation will be available at:")
    print("   http://localhost:8000/docs")