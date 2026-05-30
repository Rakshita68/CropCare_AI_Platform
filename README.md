# 🌍 Global Agriculture AI Platform

## Quick Start - One Click Launch

**Double-click this file to start everything:**
```
run_complete_system.bat
```

## Manual Start

### Option 1: Complete System
```bash
# Run this in terminal
cd "d:\new project\agriculure"
run_complete_system.bat
```

### Option 2: Individual Components
```bash
# Backend only
cd "d:\new project\agriculure"
python start_server.py

# Frontend only
# Double-click: frontend\index.html
```

## System URLs

| Component | URL |
|-----------|-----|
| **Frontend** | `file:///d:/new%20project/agriculure/frontend/index.html` |
| **Backend API** | `http://localhost:8000` |
| **API Documentation** | `http://localhost:8000/docs` |
| **Complete System** | Run `run_complete_system.bat` |

## Features

- 🌍 **6 Countries** - India, USA, Brazil, China, Australia, Argentina
- 🗣️ **17+ Languages** - Multi-language interface with real-time translation
- 🌾 **10+ Crops** - Comprehensive crop database with global varieties
- 💰 **Live Market Prices** - Real-time commodity pricing with trends
- 🤖 **Smart AI Assistant** - Works online/offline with agriculture expertise
- 📊 **Profit Analysis** - Complete business intelligence for farmers

## API Endpoints

- `POST /api/predict` - Sensor-based crop predictions
- `POST /api/gemini` - AI assistant chat
- `POST /api/crop-recommendations` - Crop cultivation guides
- `GET /api/market-prices` - Live market data

## Requirements

```bash
pip install fastapi uvicorn python-dotenv
```