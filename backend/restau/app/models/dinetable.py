from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel


class DineTable(SQLModel, table=True):
    __tablename__='dinetable'
    DineTableId : Optional[int] = Field(default=None, primary_key=True)
    IsWorkingCondition: bool = Field(default=True)
    IsCustomerOccupied : bool = Field(default=False) 
    Dinespace_FId : Optional[int] = Field(default = None, foreign_key= 'dinespace.DinespaceId')
    dinespace : Optional["Dinespace"] = Relationship(back_populates = 'dinetables') 

