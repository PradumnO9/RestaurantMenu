from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel

class Price(SQLModel , table=True):
    __tablename__='price'
    PriceId : Optional[int] = Field(default= None, primary_key=True) 
    Value: int|None = Field(default = None)