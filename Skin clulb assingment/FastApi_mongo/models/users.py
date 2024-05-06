from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    _id: str
    name: str
    email: EmailStr
    role: str
    isActive: Optional[bool]
