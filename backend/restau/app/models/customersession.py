from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from sqlmodel.main import EmailStr
from typing import Optional, List
from pydantic_extra_types.phone_numbers import PhoneNumber

from .sqllmodel import SQLModel



class CustomerSession(SQLModel, table = True):
    __tablename__ = 'customersession'
    CustomerSession: str = Field (primary_key = True)
    Qr_Fid: Optional[int] = Field(default = None)
