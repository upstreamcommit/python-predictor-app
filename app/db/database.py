from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = "sqlite:///./predictor.db"

# Connects to our database.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Used to perform actual database work.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Generates and manages a session as needed.
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()