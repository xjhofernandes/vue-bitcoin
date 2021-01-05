from service.BitcoinService import BitcoinService
from enums.Enums import Periods
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel


# teste = BitcoinService()

# nome = 'seven'
# print(Periods[nome].value)

# # print(teste.calendar_filter(datetime.datetime(2020, 12, 1), datetime.datetime(2020, 12, 31)))

# caramba = teste.period_filter(Periods[nome].value)
# print(caramba)
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}