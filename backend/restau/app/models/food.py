from sqlmodel import Field
from typing import Optional, List
from .sqllmodel import SQLModel


class Food(SQLModel,table=True):
    FoodId : Optional[int] = Field(default= None, primary_key=True)  
    FoodName : str = Field(default = '')
    FoodRegionalType_FId : Optional[int] = Field(default = None, foreign_key= 'foodregionaltype.FoodRegionalTypeId')
    FoodAllergenComment : str = Field( default = 'Not Containing Allergens')
    FoodAlert : str = Field(default = 'No Alert')
    IsAvailable : bool  = Field( default=False )
    Price_FId : Optional[int] = Field(default=None , foreign_key='price.PriceId')




# class BaseShiftTime(Duration):
#     ShiftId : PrimaryKeyConstraint(int) = Field(int, default = -1, primary_key= True)
#     StartTime : Time =  Field(Time)
#     EndTime : Time = Field(Time)


# class BaseProfileType:
#     ProfileTypeId : PrimaryKeyConstraint(int) = Field(int, default = -1, primary_key = True)
#     ProfileTypeTitle : String = Field(String, default = '')

# class BaseProfile:
#     __FirstName : String  = Field(String, default = '')
#     __MiddleName : String = Field(String, default = '')
#     __LastName : String = Field(String, default = '')
#     __NameCallable : String = Field(String, default = '')
#     __ProfileId : PrimaryKeyConstraint(int) = Field(int, default = -1, primary_key= True)
#     __PersonalEmail : String =  Field(String, default = '')
#     __PersonalContact : String = Field(String, default = '')
#     __CurrentAddress : String = Field(String, default = '')
#     __TemporaryAddress : String = Field(String, default = '')
#     __PermanentAddress : String = Field(String, default = '')
#     __PinCode : String = Field(String, default = '')
#     __NativePlace : String = Field(String, default = '')
#     __ProfileTypeId : ForeignKeyConstraint(Integer)  = Field(String, default = '')
