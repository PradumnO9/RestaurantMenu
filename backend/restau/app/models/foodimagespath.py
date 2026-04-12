from sqlmodel import Field, JSON, Column, Relationship 
from typing import Optional, List 


from .sqllmodel import SQLModel


class FoodImagesPath(SQLModel,table=True): 
    __tablename__='foodimagespath'
    FoodImagesPathId : Optional[int] = Field(default= None, primary_key=True)
    FoodImagesPathName: str = Field(default= None)
    FoodImages: List["FoodImage"]= Relationship(back_populates = "foodimagepath")  

