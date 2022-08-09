from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    # None
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None