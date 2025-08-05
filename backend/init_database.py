#!/usr/bin/env python3
"""
Database initialization script
"""
from app.core.database import SessionLocal
from app.core.init_db import init_db

def main():
    db = SessionLocal()
    try:
        init_db(db)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main() 