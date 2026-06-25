from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import User
from app.schemas.user import UserCreate, UserRead
from app.core.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserRead)
def create_user(
    user_create: UserCreate,
    db: Session = Depends(get_db),
) -> User:
    user = User(
        username=user_create.username,
        email=user_create.email,
        hashed_password=hash_password(user_create.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user