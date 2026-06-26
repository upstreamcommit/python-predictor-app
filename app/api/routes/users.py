from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import User
from app.schemas.user import UserCreate, UserRead
from app.core.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    user_create: UserCreate,
    db: Session = Depends(get_db),
) -> User:
    existing_username = (
        db.query(User)
        .filter(
                User.username==user_create.username
        )
        .first()
    )
    
    existing_user_email = (
        db.query(User)
        .filter(
                User.email==user_create.email
        )
        .first()
    )
    
    if existing_username is not None and existing_user_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with both that username and email already exists"
        )
        
    if existing_username is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that username already exists"
        )
        
    if existing_user_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with that email already exists"
        )
        
    user = User(
        username=user_create.username,
        email=user_create.email,
        hashed_password=hash_password(user_create.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user