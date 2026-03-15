from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from typing import Optional, List
from .sqllmodel import SQLModel


class Customer(SQLModel, table=True ):
    CusId : int = Field(default=None, primary_key = True)
    CusName: str =  Field(default = 'NoCustomer')
    CusAddress: str = Field(default = 'CustomerDeclines')


