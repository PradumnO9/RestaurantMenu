from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel

class Qr(SQLModel, table= True):
    QrId : Optional[int] = Field(default = None, primary_key = True)
    Qrstring: str = Field(default = None)
    Dinetable_FId: Optional[int] = Field(default = None , foreign_key = 'dinetable.DineTableId')



