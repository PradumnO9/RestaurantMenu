from sqlmodel import SQLModel,Field,ForeignKey,Relationship
from sqlmodel.main import EmailStr
from typing import Optional, List
from pydantic_extra_types.phone_numbers import PhoneNumber
from .sqllmodel import SQLModel


class Customer(SQLModel, table=True ):
    CusId : int = Field(default=None, primary_key = True)
    CusName: str =  Field(default = 'NoCustomer')
    CusAddress: str = Field(default = 'CustomerDeclines')
    CusEmail: EmailStr = Field(default = 'CustomerDeclines')
    CusPhone: PhoneNumber = Field(default = 'PhoneisMandatory')


