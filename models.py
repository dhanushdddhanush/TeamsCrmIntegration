from pydantic import BaseModel, EmailStr
from typing import Optional

class LeadCreate(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    Company: str
    Email: Optional[EmailStr]

class LeadResponse(BaseModel):
    id: str
    FirstName: Optional[str]
    LastName: Optional[str]
    Company: str
    Email: Optional[EmailStr]
