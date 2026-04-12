from sqlmodel import SQLModel

from .food import Food 
from .foodregionaltype import FoodRegionalType 
# from .price import Price 
from .qr import Qr
from .orders import Orders
from .dinetable import DineTable
from .dinespace import Dinespace
from .customer import Customer
from .customersession import CustomerSession 
from .foodimage import FoodImage
from .foodimagespath import FoodImagesPath


target_metadata = SQLModel.metadata