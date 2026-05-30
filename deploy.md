# Deployment Guide

## GitHub Repository Setup

Your codebase is now ready for GitHub! Follow these steps:

### 1. Install Git (if not already installed)
Download from: https://git-scm.com/download/windows

### 2. Initialize and Push to GitHub

```bash
# Navigate to project directory
cd "d:\new project\agriculure"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Global Agriculture AI Platform"

# Add GitHub remote (replace with your repository URL)
git remote add origin https://github.com/yourusername/agriculture-ai-platform.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `agriculture-ai-platform`
3. Description: `🌍 Global Agriculture AI Platform with multi-language support and smart farming features`
4. Make it Public or Private
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### 4. Environment Setup for Contributors
```bash
# Clone the repository
git clone https://github.com/yourusername/agriculture-ai-platform.git
cd agriculture-ai-platform

# Copy environment file
copy .env.example .env

# Edit .env and add your API keys
# GEMINI_API_KEY=your_actual_api_key_here

# Install dependencies
pip install -r requirements.txt

# Run the system
python start_server.py
```

## Files Created for GitHub:
- ✅ `.gitignore` - Excludes sensitive files
- ✅ `.env.example` - Template for environment variables
- ✅ `requirements.txt` - Python dependencies
- ✅ `LICENSE` - MIT License
- ✅ `CONTRIBUTING.md` - Contribution guidelines
- ✅ `.github/workflows/ci.yml` - GitHub Actions CI/CD

## Next Steps:
1. Install Git if needed
2. Create GitHub repository
3. Run the git commands above
4. Share your repository URL!