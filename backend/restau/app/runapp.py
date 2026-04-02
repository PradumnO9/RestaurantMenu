"""
THIS FILE DICTATES ALL API ENDPOINTS AND RUNS API APPLICATION INSTANCE.
"""
import os       # USED FOR CONNECTION STRING TO DATABASE(S)
from fastapi import FastAPI       # THE MAIN SERVER CLASS
from fastapi.routing import FastAPIError    # THE MAIN ERROR CLASS
from fastapi.responses import *   #THE RESPONSE CLASSES
from fastapi import  Request   #THE REQUEST CLASSES
from sqlmodel import create_engine,select,Session,col,func       # ORM TOOLS 
from .models.sqllmodel import Food, FoodRegionalType
from .models.sqllmodel import Customer
from .models.sqllmodel import Dinespace ,DineTable , Orders   # DECLARED MODELS

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

mainapp = FastAPI(debug =True)

"""
DATA SERVER ENGINE INSTANCE
"""
READONLYENGINE  = create_engine(os.getenv("PGDB_URL") , connect_args={  
    "options": "-c default_transaction_read_only=on"  # PostgreSQL-specific  
    }  )
READWRITEENGINE  = create_engine(os.getenv("PGDB_URL"))



"""
ADMIN APIS
"""
# FOODID REPRESENTS A SINGLE BILLABLE ITEM. 
# EDIBLE ITEM SHOWN ON MENU 

# POST  /api/login/{adminname}{hashpassword} 
@mainapp.post("/api/login/{admin_name}")
def __post_login_details(admin_name:str ,hash_password:str ):
    with open('./admin.ini','r') as admin_file:
        flag = False

        for line in  admin_file.readlines()[1:]:
            if line[:5]=='admin' and line[-23:-2] == 'creator_pradumn_kumar':
                if line[-23:-2] == admin_name:
                    flag = True
                else:
                    flag = False
            elif line[:14] == 'admin_password' and line[-22:-1]=='creator_vishal_dhokia':
                if line[-22:-1] == hash_password:
                    flag = flag and True 
                else:
                    flag= False
            
        if  flag:
            base_token = jwt.encode({ "username": admin_name, "password": hash_password })
            return ORJSONResponse(  content = {"bearer_token": base_token} , status_code = 200, headers = None, media_type = None, background= None)

        admin_file.seek(0)
        return ORJSONResponse( content = admin_file.read(), status_code = 200, headers = None, media_type = None, background= None)
        
@mainapp.get("/api/admin/menuitem/")
def __get_menu():
    try:
        with Session(READONLYENGINE) as readonlysess:
            q_menuitems =select( Food.IsAvailable
                                ,Food.FoodId
                                ,Food.FoodRegionalType
                                ,Food.FoodName
                                ,Food.FoodAllergenComment
                                ,Food.FoodAlert
                                , Food.Pricing
                                )
            result = readonlysess.exec(q_menuitems)
            return ORJSONResponse(content =  result.all(), status_code = 200, headers = None, media_type = None, background= None)
    except FastAPIError as t :
        return ORJSONResponse(content =  'database connectivity issue', status_code = 500, headers = None, media_type = None, background= None)

@mainapp.post("/api/admin/menuitem/addmenuitem")
def __post_menu_food(data:dict ):
    """
    ADMIN ADDS AN ITEM COMPLETELY.  PASSED DATA MUST HAVE SAME COLUMNS AS FOOD.
    """  
    if not data:
        return ORJSONResponse(content = 'Post Body is Empty', status_code = 200, headers = None, media_type = None, background= None)
    else:
        """
            Condition to Meet, FoodID should be <= Max(`FoodId`) from `Food.
        """
        try:
            if  data["FoodName"] and data["FoodRegionalType"] and data["FoodAllergenComment"] and data["FoodAlert"] and data["IsAvailable"] and data["is_customizable"] and data["FoodPricing"]:
                try:
                    with Session(READWRITEENGINE) as readwritesess:
                        try:
                            thisfood = Food()
                            thisfood.FoodName = data["FoodName"]
                            del data["FoodName"] 
                            thisfood.FoodRegionalType = data["FoodRegionalType"] 
                            del data["FoodRegionalType"]
                            thisfood.FoodAllergenComment = data["FoodAllergenComment"] 
                            del data["FoodAllergenComment"]
                            thisfood.FoodAlert = data["FoodAlert"] 
                            del data["FoodAllergenComment"]
                            thisfood.IsAvailable = data["IsAvailable"] 
                            del data["IsAvailable"]
                            thisfood.is_customizable = data["is_customizable"] 
                            del data["is_customizable"]
                            thisfood.FoodPricing = data["FoodPricing"]
                            del data["FoodPricing"]
                            if data:
                                return ORJSONResponse(content ='More than expected columns received',status_code = 500,headers = None,media_type = None,background= None)
                            else:
                                readwritesess.add(thisfood)
                                return ORJSONResponse(content ='Food Added Successfully',status_code = 200,headers = None,media_type = None,background= None)
                        except  e:
                            return ORJSONResponse(content = 'An Error Occurred while adding data', status_code = 200, headers = None, media_type = None, background= None)
                        readwritesess.close()
                except FastAPIError as t:
                    return ORJSONResponse(content = 'Error on FastAPI', status_code = 200, headers = None, media_type = None, background= None)       
            else:
                return ORJSONResponse(content = 'Please Add a Proper Food Data', status_code = 200, headers = None, media_type = None, background= None)
        except FastAPIError as t:
            return ORJSONResponse(content = 'Connection To Server Lost', status_code = 300, headers = None, media_type = None, background= None)
    return ORJSONResponse(content = 'Something Went Wrong', status_code = 500, headers = None, media_type = None, background= None)

@mainapp.post("/api/admin/menuitem/{FoodID}")
def __update_menu_food(FoodID:int , data:dict ):
    """
    ADMIN REPLACES AN ITEM COMPLETELY AT A FOODID. PASSED DATA MUST HAVE SAME COLUMNS AS FOODID.
    """  
    if FoodID > 0:
        try:
            max_val = float('inf')
            try:
                with Session(READONLYENGINE) as readonlysess:
                    q_menuitems =select(func.max(Food.FoodId))
                    result = readonlysess.exec(q_menuitems)
                    max_val = result.one()['FoodId']
                    print(max_val)
                    readonlysess.close()
            except:
                return ORJSONResponse(content = 'Logic Failure', status_code = 500, headers = None, media_type = None, background= None)
            if FoodID > max_val:
                return ORJSONResponse(content = 'Incorrect Input Value of FoodId', status_code = 500, headers = None, media_type = None, background= None)
        except FastAPIError as t :
            return ORJSONResponse(content =  'database connectivity issue', status_code = 500, headers = None, media_type = None, background= None)

        if not data:
            return ORJSONResponse(content = 'Post Body is Empty', status_code = 200, headers = None, media_type = None, background= None)
        else:
            """
                Condition to Meet, FoodID should be <= Max(`FoodId`) from `Food.
            """
            try:
                if  data["FoodId"] < "FoodID":
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
                                        return ORJSONResponse(content ='More than expected columns received',status_code = 500,headers = None,media_type = None,background= None)
                                    else:
                                        readwritesess.add(thatfood)
                                        return ORJSONResponse(content ='Food Updated Successfully',status_code = 200,headers = None,media_type = None,background= None)
                                except  e:
                                    return ORJSONResponse(content = 'An Error Occurred while adding data', status_code = 200, headers = None, media_type = None, background= None)
                                readwritesess.close()

                        except FastAPIError as t:
                            return ORJSONResponse(content = 'Error on FastAPI', status_code = 200, headers = None, media_type = None, background= None)       

                else:
                    return ORJSONResponse(content = 'The App just prevented a FoodItem to change check the FoodID Supplied', status_code = 200, headers = None, media_type = None, background= None)
            except FastAPIError as t:
                print("database connectivity issue")
        return ORJSONResponse(content = 'Something Went Wrong', status_code = 500, headers = None, media_type = None, background= None)
    else:
        return ORJSONResponse(content = 'Logic Failure: Negative FoodId Not Need to Pass ', status_code = 200, headers = None, media_type = None, background= None)


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

                return ORJSONResponse(  content =  'updated successful',
                                        status_code = 200,
                                        headers = None,
                                        media_type = None,
                                        background= None)
            except  e:
                print("An error occurred while querying data.")
                return Response(content = "An error occurred while querying data.", status_code=404)
            readwritesess.close()
    except FastAPIError as  t:
        print("database connectivity issue")


@mainapp.get("/api/admin/menuitem/{FoodID}")
def __get_menu_food(FoodID:int):
    try:
        with Session(READONLYENGINE) as readonlysess:
            try:
                q_fetch_menu_with_id = select(
                                 Food.IsAvailable
                                ,Food.FoodId
                                ,Food.FoodRegionalType.FoodRegionalTypeName
                                ,Food.FoodName
                                ,Food.FoodAllergenComment
                                ,Food.FoodAlert
                                ,Food.Pricing
                ).where(Food.FoodId == FoodId)
                result  = readonlysess.exec(q_fetch_menu_with_id)
                return ORJSONResponse(content = result.one(), status_code = 200, headers = None, media_type = None, background = None)
            except  e:
                return Response(content = "An error occurred while querying data.", status_code=404)
            readonlysess.close()
    except FastAPIError as t:
        return Response(content = "Database Connection Issue", status_code=404)

@mainapp.get("/api/admin/menuitemcategory/")
def __get_menu_foodregionaltype():
    try:
        with Session(READONLYENGINE) as readonlysess:
            q_fetch_menucategory = select(FoodRegionalType)
            result = readonlysess.exec(q_fetch_menucategory)
            return ORJSONResponse(content = result.all(), status_code = 200, headers = None, media_type = None , background = None)
    except:
        return Response(content = "Database Connection Issue", status_code=404)

# @mainapp.get("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __get_table_orders(table_id:int,table_qr_session_id:str ):
# """
# HELPS ADMIN TO TAKE A WATCH OF PARTICULAR TABLE BASED ON SESSION ID PROVIDED
# DISCUSS TIME AND DATE LATER AS IN SESSION DUPLICATION OCCURS JUST IN CASE THE GENERATORFACTORY IS LIKE THAT 
# ELSE ITS GOING TO BE UNIQUE 
# """
#     try:
#         with Session(READONLYENGINE) as readonlysess:
#             try:
#                 q_fetch_menu_with_id = select(Orders) #DineTable.DineTableId == table_id , Food.FoodRegionalType_FId == FoodRegionalType.FoodRegionalTypeId 
#                 result = readonlysess.exec(q_fetch_menu_with_id)
#                 return ORJSONResponse(content =  result, status_code = 200, headers = None, media_type = None, background= None)
#             except  e:
#                 print("An error occurred while querying data.")
#                 return Response(content = "An error occurred while querying data.", status_code=404)
#             readonlysess.close()
#     except FastAPIError as t:
#         print("database connectivity issue")

# @mainapp.put("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __put_table_orders(table_id:int,table_qr_session_id:str ):
#     	return Response(
#             content =  None,
#             status_code = 200,
#             headers = None,
#             media_type = None,
#             background= None
#             )

# @mainapp.post("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __post_table_orders(table_id:int,table_qr_session_id:str ):
#     	return Response(content =  None,
#                         status_code = 200,
#                         headers = None,
#                         media_type = None,
#                         background= None)

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

# #  UNKNOWN CIRCUMSTANCE
# @mainapp.patch("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
# def __patch_table_orders(table_id:int,table_qr_session_id:str ):
# 	return Response(content =  None,
#                     status_code = 200,
#                     headers = None,
#                     media_type = None,
#                     background= None)



# # DISCARDS FROM RESTAURANT MENU 
# @mainapp.delete("/api/admin/menu/{FoodID}")
# def __delete_menu_food(FoodID:int):
#     try:
#         with Session(READWRITEENGINE) as readwritesess:
#             try:
#                 qdelete(Food).where(Food.FoodId ==FoodID )
#                 result = readwritesess.exec()
#                 return ORJSONResponse(  content =  'Deleted Successfully',
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
#     return ORJSONResponse(content =  None, status_code = 200, headers = None, media_type = None, background= None)
# # FULLMENU DISPLAYED
# # READONLY

# @mainapp.get("/api/admin/menucategory/")
# def __get_menu():
#     try:
#         with Session(READONLYENGINE) as readwritesess:
#             try:
#                 q_statement = select(FoodRegionalType)
#                 result = readwritesess.exec(q_statement)
#                 ORJSONResponse(content =  result, status_code = 200, headers = None, media_type = None, background= None)
#             except:
                
# 	return ORJSONResponse(content =  None, status_code = 200, headers = None, media_type = None, background= None)

# # HISTORY FOR EACH DATE OF YEAR IS KEPT.

# @mainapp.get("/api/admin/order-history/{order-date}")
# def __get_order_history():
# 	return Response(content =  None,
#     status_code = 200,
#     headers = None,
#     media_type = None,
#     background= None)

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


# # User FULLMENU DISPLAYED
# # User READONLY
# @mainapp.get("/api/menu/")
# def __get_menu():
#     try:
#         with Session(READONLYENGINE) as readonlysess:
#             try:
#                 q_fetch_menu = select(Food,Price,FoodRegionalType)
#                 result = readonlysess.exec(q_fetch_menu)
#                 return ORJSONResponse(  
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
# 	return ORJSONResponse(content =  None, status_code = 200, headers = None, media_type = None, background= None)



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


		
		
		 
	




	
	
	
		 