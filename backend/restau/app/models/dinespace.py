from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel



class Dinespace(SQLModel , table=True):
    DinespaceId : Optional[int] = Field(default=None, primary_key=True)
    DinespaceName:  str = Field(default = '') 
    # Tables :List[DineTable] = Relationship(back_populates='DineTable') 

