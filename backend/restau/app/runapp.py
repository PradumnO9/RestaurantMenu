import os
from fastapi.applications import FastAPI
from fastapi.routing import FastAPIError
from fastapi.responses import Response, ORJSONResponse, UJSONResponse
from sqlmodel import create_engine

mainapp = FastAPI()
engine  = create_engine(os.getenv("PGDB_URL"))
from .app.models import Food, FoodRegionalType, Price


@app.get("/api/admin/table-orders/{table_id}/{table_qr_session_id}"):
def __get_table_orders(table_id:int,table_qr_session_id:str ):
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
    
@app.put("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __put_table_orders(table_id:int,table_qr_session_id:str ):

    	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.post("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __post_table_orders(table_id:int,table_qr_session_id:str ):
    	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.delete("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __delete_table_orders(table_id:int,table_qr_session_id:str ):
    	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.patch("/api/admin/table-orders/{table_id}/{table_qr_session_id}")
def __patch_table_orders(table_id:int,table_qr_session_id:str ):
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)

@app.get("/api/admin/menu/{FoodID}",response_class=ORJSONResponse)
def __get_menu_food(FoodID:int):
	ORJSONResponse(content: typing.Any = Food().get("FoodID"=1),
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.put("/api/admin/menu/{FoodID}")
def __put_menu_food(FoodID:int):
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.post("/api/admin/menu/{FoodID}")
def __post_menu_food(FoodID:int):
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.delete("/api/admin/menu/{FoodID}")
def __delete_menu_food(FoodID:int):
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)

@app.get("/api/admin/menu/")
def __get_menu():
	ORJSONResponse(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.get("/api/admin/order-history/{order-date}")
def __get_order_history():
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)
@app.get("/api/admin/order-ETA/{}")
def __get_order_eta():
	Response(content: typing.Any = None,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTask | None = None,)



=========================
ADMIN Auth.
=========================
/frontend client apis 
	USES /api/admin/[endpoints for backend ]
		GET POST PUT PATCH DELETE
			/api/admin/table-orders/{table_id}/{table_qr_session_id}
			# tables will be in sync with qr information table metadata. [i.e. tableid]
		GET PUT POST DELETE		
			/api/admin/menu/{FoodID}
        	GET 
			/api/admin/menu/ # FULL DISPLAY 
			/api/admin/order-history/{order-date}   # /{order-duration}
			/api/admin/order-ETA/{}

==============================
TABLE API Endpoints [Customer]
===============================
.frontend 
		addtocart handled by Redux
.backend
		POST 
			/api/table-order/:session_id/:table_id
			
		GET 
			/api/admin/menu/ # FULL DISPLAY




classes 2 table. 
	menu information
	passwordless table information with 1 admin[WP] role. 
		name , mobile number 
 logs history table 
	session information
	user and table information
	table qr scanned info.


		
		
		 
	




	
	
	
		 