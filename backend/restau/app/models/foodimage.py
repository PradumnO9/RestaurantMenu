from sqlmodel import Field, JSON, Column, Relationship 
from typing import Optional, List 
from .sqllmodel import SQLModel

class FoodImage(SQLModel,table=True): 
    FoodImageId : Optional[int] = Field(default= None, primary_key=True)
    Food_FId : Optional[int] = Field(default = None, foreign_key= 'food.FoodId')
    FoodImageFileName: str = Field(default = None )
    FoodImagePath_Fid: Optional[int] = Field(default=None, foreign_key = 'food.FoodId'  ) 
    class Config:
        arbitrary_types_allowed=True 


