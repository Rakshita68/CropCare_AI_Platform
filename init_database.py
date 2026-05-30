import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.database import engine
from backend.app import models

async def init_db():
    """Initialize the database with tables"""
    print("Initializing database...")
    
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(models.Base.metadata.create_all)
        print("Database tables created successfully!")
    
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())