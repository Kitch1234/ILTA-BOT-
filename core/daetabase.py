import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

db = None


async def connect_db():
    global db

    db = await asyncpg.create_pool(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    print("✅ PostgreSQL подключён")


async def close_db():
    global db

    if db:
        await db.close()
        print("❌ PostgreSQL отключён")
