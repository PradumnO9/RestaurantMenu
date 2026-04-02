from sqlmodel import Field, JSON, Column, Relationship 
from typing import Optional, List 
from .sqllmodel import SQLModel


class FoodImagesPath(SQLModel,table=True): 
    FoodImagesPathId : Optional[int] = Field(default= None, primary_key=True)
    FoodImagesPathName: str = Field(default= None)
