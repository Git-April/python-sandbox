from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class Item(BaseModel):
  name:str
  price:float
  is_offer: bool | None = None

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q: str | None = None):
  return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  to_dataframe(item)
  return {"item_name": item.name, "item_id": item_id}

def to_dataframe(item:Item):
  df = pd.Series({"item_name": item.name, "item_price": item.price})
  print(df)