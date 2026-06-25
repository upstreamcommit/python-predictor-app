from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
        
    created_at: datetime
    updated_at: datetime | None
    
    model_config = ConfigDict(from_attributes=True)