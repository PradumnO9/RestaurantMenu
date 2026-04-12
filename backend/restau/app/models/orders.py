from sqlmodel import SQLModel,Field,ForeignKey,Relationship

from typing import Optional, List
import datetime

from .sqllmodel import SQLModel

class Orders(SQLModel, table=True):
    __tablename__='orders'
    OrderId : Optional[int] = Field(default= None,primary_key = True)
    Customer_FId: Optional[int] = Field(default = None, foreign_key= 'customer.CusId') #repeating customer
    Dinetable_FId :  Optional[int] = Field(default = None, foreign_key= 'dinetable.DineTableId')
    # Dine_Table: DineTable  = Relationship( back_populates = "DineTable")
    Transaction_FId: str = Field(default = None, foreign_key = '' )
    OrderTimeStamp : datetime.datetime = Field(default = datetime.datetime.now())


