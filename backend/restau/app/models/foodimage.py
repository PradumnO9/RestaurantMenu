from sqlmodel import SQLModel, Field, JSON, Column, Relationship 
from typing import Optional, List 
from .sqllmodel import SQLModel

class FoodImage(SQLModel,table=True): 
    __tablename__ = 'foodimage'
    FoodImageId : Optional[int] = Field(default= None, primary_key=True)
    FoodImageFileName: str = Field(default = None )
    
    FoodImagePath_FId: Optional[int] = Field(default=None, foreign_key = 'foodimagespath.FoodImagesPathId'  ) 
    
    FoodviaImage: List["Food"]= Relationship(back_populates = "foodimage")  
    
    foodimagepath: Optional["FoodImagesPath"] = Relationship(back_populates = "FoodImages" )
    class Config:
        arbitrary_types_allowed=True 


