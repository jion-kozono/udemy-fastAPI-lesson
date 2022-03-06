from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# # パスパラメータ
# # 上から順に関数が実行されるため、順番が大事

# @app.get("/countries/japan")
# async def japan():
#     return {"message": 'This is Japan!'}

# @app.get("/countries/{country_name}")
# async def country(country_name: str):
#     return {"country_name": country_name}

# # クエリパラメータ
# @app.get("/countries/{country_name}")
# async def country(country_name: str = 'japan', city_name: str = 'tokyo'):
#     return {
#         "country_name": country_name,
#         "city_name": city_name
#     }

# # オプションパラメータ
# @app.get("/countries/")
# async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
#     return {
#         "country_name": country_name,
#         "country_no": country_no
#     }

# post
class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items: List[Item]

# @app.post("/item/")
# async def create_item(item: Item):
#     return {"message": f"{item.name}は、税込価格{int(item.price *item.tax)}円です。"}

@app.post("/")
async def index(data: Data):
    return {"data": data}