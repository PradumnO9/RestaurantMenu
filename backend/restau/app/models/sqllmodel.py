from sqlmodel import SQLModel

from .food import Food 
from .foodregionaltype import FoodRegionalType 
from .price import Price 

target_metadata = SQLModel.metadata