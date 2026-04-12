"""
THIS FILE DICTATES ALL API ENDPOINTS AND RUNS API APPLICATION INSTANCE.
"""
import os       # USED FOR CONNECTION STRING TO DATABASE(S)
from fastapi import FastAPI       # THE MAIN SERVER CLASS
from fastapi.encoders import jsonable_encoder
from fastapi.routing import FastAPIError    # THE MAIN ERROR CLASS
from fastapi.responses import *   #THE RESPONSE CLASSES
from fastapi.logger import logger
from fastapi import  Request,File,WebSocket   #THE REQUEST CLASSES
from sqlmodel import create_engine,select,Session,col,func       # ORM TOOLS 
from .models.sqllmodel import Food, FoodRegionalType, Dinespace ,DineTable , Orders,Customer


import jwt

from fastapi.middleware.cors import CORSMiddleware


"""
Orders.OrderId
Orders.Customer_FId
Orders.Dinetable_FId
Orders.Transaction_FId
Orders.OrderTimeStamp

Dinespace.DinespaceId
Dinespace.DinespaceName

DineTable.DineTableId
DineTable.IsWorkingCondition
DineTable.IsCustomerOccupied
DineTable.Dinespace_FId

FoodRegionalType.FoodRegionalTypeId
FoodRegionalType.FoodRegionalTypeName

Food.FoodId 
Food.FoodName 
Food.FoodRegionalType_FId 
Food.FoodAllergenComment 
Food.FoodAlert 
Food.IsAvailable 
Food.Price_FId 

CustomerSession.CustomerSession
CustomerSession.Qr_Fid

Customer.CusId
Customer.CusName
Customer.CusAddress
Customer.CusEmail
Customer.CusPhone

"""
"""
BACKEND SERVER INSTANCE
"""
origins = [
    "http://localhost",
    "http://localhost:8080"
]
mainapp = FastAPI(debug =True)
mainapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
DATA SERVER ENGINE INSTANCE
"""
READONLYENGINE  = create_engine(os.getenv("PGDB_URL") , connect_args={  
    "options": "-c default_transaction_read_only=on"  # PostgreSQL-specific  
    }  )
READWRITEENGINE  = create_engine(os.getenv("PGDB_URL"))
# @mainapp.websocket("/ws")


"""
HELPER
"""


"""
ADMIN APIS
"""
# FOODID REPRESENTS A SINGLE BILLABLE ITEM. 
# EDIBLE ITEM SHOWN ON MENU 

# POST  /api/login/{adminname}{hashpassword} 
@mainapp.post("/api/login/")
def __post_login_details(data:dict):
    admin_name ,hash_password = data["admin_name"], data["hash_password"]
    with open('./app/admin.ini','r') as admin_file:
        authenticate = False
        for line in  admin_file.readlines()[1:]:
            if line[:5]=='admin' and line[-23:-2] == 'creator_pradumn_kumar':
                if line[-23:-2] == admin_name:
                    authenticate = True
                else:
                    authenticate = False
            elif line[:14] == 'admin_password' and line[-22:-1]=='creator_vishal_dhokia':
                if line[-22:-1] == hash_password:
                    authenticate = authenticate and True 
                else:
                    authenticate= False
            
        if  authenticate:
            base_token = jwt.encode(key = 'tramp',payload={ "username": admin_name, "password": hash_password})
            return JSONResponse( content = {"type":"admin","bearer_token": base_token} , status_code = 200, headers = None, media_type = None, background= None)

        admin_file.seek(0)
        return JSONResponse( content = admin_file.read(), status_code = 200, headers = None, media_type = None, background= None)
        
@mainapp.get("/api/admin/menuitem/")
def __get_menu_food():
    try:
        with Session(READONLYENGINE) as readonlysess:
            q_menuitems =select(Food.IsAvailable, Food.FoodId, FoodRegionalType.FoodRegionalTypeName, Food.FoodName, Food.FoodAllergenComment, Food.FoodAlert, Food.FoodPricing).where(Food.FoodRegionalType_FId == FoodRegionalType.FoodRegionalTypeId)
            menuitems_fetched = readonlysess.exec(q_menuitems)
            # l = [list(menuitems_fetched.keys())]
            # l .append([list(x) for x in menuitems_fetched.all()])
            return JSONResponse(content = jsonable_encoder(menuitems_fetched.mappings().all()) , status_code = 200, headers = None, media_type = None, background= None)
    except FastAPIError as t :  
        return JSONResponse(content = {"message":"database connectivity issue"}, status_code = 500, headers = None, media_type = None, background= None)

@mainapp.post("/api/admin/menuitem/addmenuitem/")
def __post_menu_food(data:dict):
    """
    ADMIN ADDS AN ITEM COMPLETELY.  PASSED DATA MUST HAVE SAME COLUMNS AS FOOD.
    """  
    if not data:
        return JSONResponse(content = {"message":"Post Body is Empty"}, status_code = 200, headers = None, media_type = None, background= None)
    else:
        # Condition to Meet, FoodID should be <= Max(`FoodId`) from `Food.
        try:
            if  data["FoodName"] and  data["FoodPricing"]:  
                try:
                    with Session(READWRITEENGINE) as readwritesess:
                        try:
                            # Logic to add Model basis 
                            # logic for verifying if Food Region Exists already.
                            q_check_food_regional_type = select(FoodRegionalType).where(FoodRegionalType.FoodRegionalTypeName == data["FoodRegionalType"])
                            food_regional_type_lookup_result= readwritesess.exec(q_check_food_regional_type).one()

                            if food_regional_type_lookup_result is not None:
                                data["FoodRegionalType"] = food_regional_type_lookup_result.FoodRegionalTypeId
                            else:
                                return JSONResponse(content={"message":"Correct FoodRegionalType Needed. If not exist already then create new first"},status_code = 200,headers = None,media_type = None,background= None)
                            
                            # logic for adding just Food Model data
                            thisfood = Food()
                            
                            thisfood.FoodName = data["FoodName"]
                            del data["FoodName"] 
                        
                            thisfood.FoodRegionalType_FId = data["FoodRegionalType"] 
                            del data["FoodRegionalType"]

                            if data["FoodAllergenComment"]:
                                thisfood.FoodAllergenComment = data["FoodAllergenComment"] 
                            del data["FoodAllergenComment"]
                            if data["FoodAlert"]:
                                thisfood.FoodAlert = data["FoodAlert"] 
                            del data["FoodAlert"]

                            thisfood.IsAvailable = bool(data["IsAvailable"]) 
                            del data["IsAvailable"]
                            thisfood.is_customizable = bool(data["is_customizable"]) 
                            del data["is_customizable"]
                            thisfood.FoodPricing = data["FoodPricing"]
                            del data["FoodPricing"]
                        
                            with open(f'./images/"{thisfood.FoodId}_{thisfood.FoodName.replace(' ','-')}.{data["File"].split('.')[-1]}"', "x") as creatable_food_image :
                                creatable_food_image.write(data.FILE)
                                creatable_food_image.close()
                            del data["File"]

                            if data:
                                return JSONResponse(content = {"message":"More than expected columns received"},status_code = 200,headers = None,media_type = None,background= None)
                            else:
                                readwritesess.add(thisfood)
                                readwritesess.commit()
                                readwritesess.close()

                                return JSONResponse(content = {"message":"Food Added Successfully"},status_code = 200,headers = None,media_type = None,background= None)
                        except KeyError as e :
                            readwritesess.close()
                            return JSONResponse(content = {"message":f"{e}"}, status_code = 200, headers = None, media_type = None, background= None)
                except FastAPIError as t:
                    return JSONResponse(content = {"message":"Error on FastAPI"}, status_code = 500, headers = None, media_type = None, background= None)       
            else:
                return JSONResponse(content = {"message":"Please Add a Proper Food Data"}, status_code = 200, headers = None, media_type = None, background= None)
        except FastAPIError as t:
            return JSONResponse(content = 'Connection To Server Lost', status_code = 300, headers = None, media_type = None, background= None)
    return JSONResponse(content = 'Something Went Wrong', status_code = 500, headers = None, media_type = None, background= None)

@mainapp.post("/api/admin/menuitem/{FoodID}")
def __update_menu_food(FoodID:int , data:dict ):
    """
    ADMIN REPLACES AN ITEM COMPLETELY AT A FOODID.
    PASSED DATA MUST HAVE SAME COLUMNS AS FOODID.
    """  

    if FoodID > 0:
        try:
            # whats the largest available FoodID
            max_val = float('inf')
            try:
                with Session(READONLYENGINE) as readonlysess:
                    q_count_total =select(func.max(Food.FoodId))
                    result = readonlysess.exec(q_count_total)
                    max_val = result.one()['FoodId']
                    readonlysess.close()
            except:
                return JSONResponse(content = {"message":"Logic Failure"}, status_code = 500, headers = None, media_type = None, background= None)
            # if that id is correct.
            if FoodID > max_val:
                return JSONResponse(content = {"message":"Incorrect Input Value of FoodId"}, status_code = 500, headers = None, media_type = None, background= None)
        except FastAPIError as t :
            return JSONResponse(content = {"message":"database connectivity issue"}, status_code = 500, headers = None, media_type = None, background= None)
        # if data is none
        if not data:
            return JSONResponse(content = {"message":"Post Body is Empty"}, status_code = 200, headers = None, media_type = None, background= None)
        else:
            # Condition to Meet, FoodID should be <= Max(`FoodId`) from `Food`.
            try:
                if data["FoodId"] == FoodID:
                    if  data["FoodId"] and data["FoodName"] and data["FoodRegionalType"] and data["FoodAllergenComment"] and data["FoodAlert"] and data["IsAvailable"] and data["is_customizable"] and data["FoodPricing"]:
                        try:
                            with Session(READWRITEENGINE) as readwritesess:
                                try:
                                    q_fetch_menu_with_id = select(Food).where(Food.FoodId == data["FoodId"])
                                    result = readwritesess.exec(q_fetch_menu_with_id)
                                    thatfood = result.one()
                                    thatfood.FoodName = data["FoodName"]
                                    del data["FoodName"] 
                                    thatfood.FoodRegionalType = data["FoodRegionalType"] 
                                    del data["FoodRegionalType"]
                                    thatfood.FoodAllergenComment = data["FoodAllergenComment"] 
                                    del data["FoodAllergenComment"]
                                    thatfood.FoodAlert = data["FoodAlert"] 
                                    del data["FoodAllergenComment"]
                                    thatfood.IsAvailable = data["IsAvailable"] 
                                    del data["IsAvailable"]
                                    thatfood.is_customizable = data["is_customizable"] 
                                    del data["is_customizable"]
                                    thatfood.FoodPricing = data["FoodPricing"]
                                    del data["FoodPricing"]
                                    if data:
                                        return JSONResponse(content = {"message":"More than expected columns received"},status_code = 500,headers = None,media_type = None,background= None)
                                    else:
                                        readwritesess.add(thatfood)
                                        return JSONResponse(content ={"message":"Food Updated Successfully"},status_code = 200,headers = None,media_type = None,background= None)
                                except  e:
                                    return JSONResponse(content = {"message":"An Error Occurred while adding data"}, status_code = 200, headers = None, media_type = None, background= None)
                                readwritesess.close()

                        except FastAPIError as t:
                            return JSONResponse(content = {"message":"Error on FastAPI"}, status_code = 200, headers = None, media_type = None, background= None)       

                else:
                    return JSONResponse(content = {"message":"The App just prevented a FoodItem to change check the FoodID Supplied"}, status_code = 200, headers = None, media_type = None, background= None)
            except FastAPIError as t:
                print("database connectivity issue")
        return JSONResponse(content = {"message":"Something Went Wrong"}, status_code = 500, headers = None, media_type = None, background= None)
    else:
        return JSONResponse(content = {"message":"Logic Failure: Negative FoodId Not Need to Pass"}, status_code = 200, headers = None, media_type = None, background= None)

@mainapp.patch("/api/admin/menu/{FoodID}")
def __put_menu_food(FoodID:int, Data:dict):
    """
    # Admin updates a missing property  
    """
    try:
        with Session(READWRITEENGINE) as readwritesess:
            try:
                q_fetch_menu_with_id = select(Food).where(Food.FoodId == FoodID)
                result = readwritesess.exec(q_fetch_menu_with_id)
                food = result.one()
                if getattr(food, Data["column"]) != None:
                    setattr(food, Data["column"], Data["value"])

                return JSONResponse(  content =  'updated successful',
                                        status_code = 200,
                                        headers = None,
                                        media_type = None,
                                        background= None)
            except  e:
                return Response(content = {"message":"An error occurred while querying data."}, status_code=404)
            readwritesess.close()
    except FastAPIError as  t:
        print("database connectivity issue")


@mainapp.get("/api/admin/menuitem/{FoodID}")
def __get_menu_food(FoodID:int):
    print(FoodID)
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_menu_with_id = select(Food.IsAvailable, Food.FoodId, FoodRegionalType.FoodRegionalTypeName, Food.FoodName, Food.FoodAllergenComment, Food.FoodAlert, Food.FoodPricing).join(FoodRegionalType).where( ((Food.FoodId == FoodID) and Food.FoodRegionalType_FId == FoodRegionalType.FoodRegionalTypeId))
                menuitem_fetched = readonlysess.exec(q_fetch_menu_with_id)
                l = [list(menuitem_fetched.keys())]
                l.append([list(x) for x in menuitem_fetched.all()])
                return JSONResponse(content = l, status_code = 200, headers = None, media_type = None, background = None)
            except :
                readonlysess.close()
                return Response(content = {"message":"An error occurred while querying data."}, status_code=404, headers = None, media_type = None, background = None)
            
    except FastAPIError as t:
        return Response(content = {"message":"Database Connection Issue"}, status_code=404, headers = None, media_type = None, background = None)

# OLD BUT USEFUL SOMEDAY
# @mainapp.get("/api/admin/menuitemcategory/")
# def __get_menu_foodregionaltype():
#     try:
#         with Session(READONLYENGINE) as readonlysess:
#             q_fetch_menucategory = select(FoodRegionalType.FoodRegionalTypeId,FoodRegionalType.FoodRegionalTypeName)
#             result = readonlysess.exec(q_fetch_menucategory)
#             return JSONResponse(content = dict(result.all()),status_code = 200, headers = None, media_type = None , background = None)
#     except FastAPIError as e:
#         return JSONResponse(content ={"message":"Database Connection Issue "}, status_code=404, headers = None, media_type = None, background = None)

@mainapp.get("/api/admin/menuitemcategory/")
def __get_menu_foodregionaltype():
    try:
        with Session(READONLYENGINE) as readonlysess:
            q_fetch_menucategory = select(FoodRegionalType.FoodRegionalTypeId,FoodRegionalType.FoodRegionalTypeName)
            result = readonlysess.exec(q_fetch_menucategory)
            # print(result.mappings().all())
            return JSONResponse(content = jsonable_encoder(result.mappings().all()),status_code = 200, headers = None, media_type = None , background = None)
    except FastAPIError as e:
        return JSONResponse(content ={"message":"Database Connection Issue "}, status_code=404, headers = None, media_type = None, background = None)

@mainapp.post("/api/admin/menucategory/addmenucategory")
def __post_add_menu_foodregionaltype(menucategory:str ):
    """
    Adds a foodregionaltype aka. category
    """
    try:
        result = None
        with Session(READONLYENGINE) as readonlysess:
            q_fetch_menucategory = select(FoodRegionalType.FoodRegionalTypeId).where(FoodRegionalType.FoodRegionalTypeName == menucategory)
            menucategory_fetched = readonlysess.exec(q_fetch_menucategory)
            result = menucategory_fetched.first()     
            

        if not result:            
            with Session(READWRITEENGINE) as readwritesess:
                thiscategory = FoodRegionalType()
                thiscategory.FoodRegionalTypeName=menucategory
                readwritesess.add(thiscategory) 
                readwritesess.commit()               
                return JSONResponse(content = {"message":"Addition of category successful."}, status_code = 200, headers = None, media_type = None , background = None)
        else:
            return JSONResponse(content = {"message":"This category already exists", "Id": result }, status_code = 200, headers = None, media_type = None , background = None )

    except FastAPIError as e:
        return JSONResponse(content = {"message":"Database Connection Issue" }, status_code=404)



@mainapp.get("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __get_table_orders(table_id:int,table_qr_session_id:str ):
    """
    HELPS ADMIN TO TAKE A WATCH OF PARTICULAR TABLE BASED ON SESSION ID PROVIDED
    DISCUSS TIME AND DATE LATER AS IN SESSION DUPLICATION OCCURS JUST IN CASE THE GENERATORFACTORY IS LIKE THAT 
    ELSE ITS GOING TO BE UNIQUE 
    """
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_tableorder_with_id = select(Orders.OrderId,Customer.CusName,Orders.Dinetable_FId,Orders.Transaction_FId,Orders.OrderTimeStamp,Dinespace.DinespaceName).where(((Orders.Customer_FId==Customer.CusId) and Orders.Dinetable_FId == DineTable.DineTableId) and DineTable.Dinespace_FId == Dinespace.DinespaceId)
                result = readonlysess.exec(q_fetch_tableorder_with_id)
                return JSONResponse(content=jsonable_encoder(result.mappings().all()),status_code=200,headers=None,media_type=None,background=None)
            except  :
                readonlysess.close()
                return JSONResponse(content={"message":"An error occurred while querying data."}, status_code=404)
    except FastAPIError as t:
        return JSONResponse(content={"message":"Database Connectivity Issue"}, status_code=404)


@mainapp.put("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __put_table_orders(table_id:int,table_qr_session_id:str ):
    """
    Helps admin to take responsibility of modifying order.
    """
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_tableorder_with_id = select(Orders.OrderId,Customer.CusName,Orders.Dinetable_FId,Orders.Transaction_FId,Orders.OrderTimeStamp,Dinespace.DinespaceName).where(((Orders.Customer_FId==Customer.CusId) and Orders.Dinetable_FId == DineTable.DineTableId) and DineTable.Dinespace_FId == Dinespace.DinespaceId)
                result = readonlysess.exec(q_fetch_tableorder_with_id)
                return JSONResponse(content=jsonable_encoder(result.mappings().all()),status_code=200,headers=None,media_type=None,background=None)
            except  :
                readonlysess.close()
                return JSONResponse(content={"message":"An error occurred while querying data.", "type":"admin"}, status_code=404)
    except FastAPIError as t:
        return JSONResponse(content={"message":"Database Connectivity Issue"}, status_code=404)

# @mainapp.post("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __post_table_orders(table_id:int,table_qr_session_id:str ):
#     """
#     Helps admin to take responsibility of modifying order.
#     """

#     return JSONResponse(content =  {}, status_code = 200, headers = None, media_type = None, background= None)

# # DELETE WAS KEPT HERE JUST IN CASE THE CUSTOMER LEAVES MID MEAL 
# # OR MEAL ORDERED WAS REJECTED BY RESTAURANT PEOPLE DUE TO UNFORESEEN 
# # CIRCUMSTANCE

# @mainapp.delete("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __delete_table_orders(table_id:int,table_qr_session_id:str ):
#     	return Response(content =  None,
#                         status_code = 200,
#                         headers = None,
#                         media_type = None,
#                         background= None)

#  UNKNOWN CIRCUMSTANCE
@mainapp.patch("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __patch_table_orders(table_id:int,table_qr_session_id:str ):

	return JSONResponse(content =  None,status_code = 200,headers = None,media_type = None,background= None)



# # DISCARDS FROM RESTAURANT MENU 
# @mainapp.delete("/api/admin/menu/{FoodID}")
# def __delete_menu_food(FoodID:int):
#     try:
#         with Session(READWRITEENGINE) as readwritesess:
#             try:
#                 qdelete(Food).where(Food.FoodId ==FoodID )
#                 result = readwritesess.exec()
#                 return JSONResponse(  content =  'Deleted Successfully',
#                                         status_code = 200,
#                                         headers = None,
#                                         media_type = None,
#                                         background= None)
#             except  e:
#                 print("An error occurred while querying data.")
#                 return Response(content = "An error occurred while querying data.", status_code=404)
#             readwritesess.close()
#     except FastAPIError  as t:
#         print("database connectivity issue")
#     return JSONResponse(content =  None, status_code = 200, headers = None, media_type = None, background= None)
# # FULLMENU DISPLAYED
# # READONLY

@mainapp.get("/api/admin/menucategory/")
def __get_menu():
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_menucategory = select(FoodRegionalType.FoodRegionalTypeId, FoodRegionalType.FoodRegionalTypeName)
                result = readonlysess.exec(q_fetch_menucategory)
                JSONResponse(content =  jsonable_encoder(result.mappings().all()), status_code = 200, headers = None, media_type = None, background= None)
            except:
                return JSONResponse(content =  {"message": "there was an issue querying data", "type":"admin"}, status_code = 200, headers = None, media_type = None, background= None)
    except FastAPIError :
        return JSONResponse(content = {"message":"Database connectivity issue"}, status_code = 200, headers = None, media_type = None, background= None)

# # HISTORY FOR EACH DATE OF YEAR IS KEPT.

@mainapp.get("/api/admin/order-history/{order-date}")
def __get_order_history():
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_order_history = select(Orders.OrderId,Orders.OrderTimeStamp, Customer.CusId, Customer.CusEmail,Customer.CusPhone, Orders.Dinetable_FId).where({Orders.Customer_FId == Customer.CusId})
                result = readonlysess.exec(q_fetch_order_history)
                JSONResponse(content =  jsonable_encoder(result.mappings().all()), status_code = 200, headers = None, media_type = None, background= None)
            except:
                return JSONResponse(content =  {"message": "there was an issue querying data", "type":"admin"}, status_code = 200, headers = None, media_type = None, background= None)
    except FastAPIError :
        return JSONResponse(content = {"message":"Database connectivity issue"}, status_code = 200, headers = None, media_type = None, background= None)

# # DINE IN  TAKES TIME TO PREPARE FOOD 
# # WHAT AND HOW MUCH BASED ON PREVIOUS RECORDED ENTRIES 
# # WILL BE SHOWN IN APP

# @mainapp.get("/api/admin/order-ETA/{}")
# def __get_order_eta():
# 	return Response(content =  None,
#                     status_code = 200,
#                     headers = None,
#                     media_type = None,
#                     background= None)


# User FULLMENU DISPLAYED
# User READONLY
# @mainapp.get("/api/menu/")
# def __get_menu():
#     try:
#         with Session(READONLYENGINE) as readonlysess:
#             try:
#                 q_fetch_menu = select(Food.FoodId, Food.FoodName, Food.FoodAlert, Food.Food,Price,FoodRegionalType).where()
#                 result = readonlysess.exec(q_fetch_menu)
#                 return JSONResponse(  
#                     content =  result,
#                     status_code = 200,
#                     headers = None,
#                     media_type = None,
#                     background= None
#                 )
#             except  e:
#                 print("An error occurred while querying data.")
#                 return Response(content = "An error occurred while querying data.", status_code=404)
#             readonlysess.close()
#     except FastAPIError as t:
#         print("database connectivity issue")

#     q_statement=select(Food,Price,FoodRegionalType)
# 	return JSONResponse(content =  None, status_code = 200, headers = None, media_type = None, background= None)



# # =========================
# # ADMIN Auth.
# # =========================
# # /frontend client apis 
# # 	USES /api/admin/[endpoints for backend ]
# # 		GET POST PUT PATCH DELETE
# # 			/api/admin/table-orders/{table_id}/{table_qr_session_id}
# # 			
#             # tables will be in sync with qr information table metadata. [i.e. tableid]
# # 		GET PUT POST DELETE		
# # 			/api/admin/menu/{FoodID}
# #            
# #     	GET 
# # 			/api/admin/menu/ # FULL DISPLAY 
# # 			/api/admin/order-history/{order-date}   # /{order-duration}
# # 			/api/admin/order-ETA/{}
# #       SingleAdmin no verification.
# #       /api/login/{adminname}{hashpassword} 
# #            redirect to GET /api/admin/menuitem
# #             also needs GET /api/admin/menucategory
# #               onclick  GET /api/admin/menuitem/{FoodId}
# #                    Update per menuitem  PATCH /api/admin/menuitem/{FoodId} body:{"colname":"value"}
# #               For adding menu item        POST /api/admin/menuitem/{FoodId}  
# #               For delete  menu item        DELETE /api/admin/menuitem/{FoodId}  
# #       need to contact to change email to company.
# #       
# #       Multiadmin
# #       POST 
# #          /api/login/{adminname}{hashpassword}  
# #          /api/update_password/{useremail}
# #       PATCH 
# #           /api/update_password+some_token/{useremail}?{}


# # ==============================
# # TABLE API Endpoints [Customer]
# # ===============================
# # .frontend 
# # 		addtocart handled by Redux
# # .backend
# # 		POST 
# # 			/api/table-order/:session_id/:table_id
			
# # 		GET 
# # 			/api/admin/menu/ # FULL DISPLAY




# # classes 2 table. 
# # 	menu information
# # 	passwordless table information with 1 admin[WP] role. 
# # 		name , mobile number 
# #  logs history table 
# # 	session information
# # 	user and table information
# # 	table qr scanned info.

## one hour after session expires... no more orders accepted. 
## 

		
		
		 
	




	
	
	
		 