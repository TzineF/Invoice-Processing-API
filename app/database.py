

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is missing")

# Explicitly select the already installed Psycopg 3 driver
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connected:", result.scalar())

if __name__ == "__main__":
    test_connection()
