from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel

class FoodRegionalType(SQLModel,table=True):
    FoodRegionalTypeId : Optional[int] =  Field( primary_key=True)  
    FoodRegionalTypeName :str = Field( default='')

