from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

# ------------------------------------------------------------
# DATABASE URL
# ------------------------------------------------------------
DATABASE_URL = "sqlite:///./app.db"

# ------------------------------------------------------------
# SQLAlchemy Engine
# ------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Only for SQLite
)

# ------------------------------------------------------------
# Session Factory
# ------------------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ------------------------------------------------------------
# Base Model (for all SQLAlchemy models)
# ------------------------------------------------------------
Base = declarative_base()

# ------------------------------------------------------------
# FastAPI Database Dependency
# ------------------------------------------------------------
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
