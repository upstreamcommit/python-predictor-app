from app.db.base import Base
from app.db.database import engine
from app.models import User

def init_db() -> None:
    Base.metadata.create_all(bind=engine)