from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel
import datetime

class Order(SQLModel, table=True)
    OrderId : Optional[int] = Field(default= None, table=True)
    Customer_FId: Optional[int] = Field(default = None, foreignkey= 'customer.CusId')
    Dinetable_FId :  Optional[int] = Field(default = None, foreignkey= 'dinetable.DineTableId')
    # Transaction_FId: str = Field(default = None, foreign_key = '' )
    OrderTimeStamp : datetime.datetime = Field(default = datetime.datetime.now())


