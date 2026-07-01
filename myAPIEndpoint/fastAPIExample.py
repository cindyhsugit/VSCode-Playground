from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {1: "Apple", 2:"Banana"}

class Item(BaseModel):
    name: str

#retrieve an item
@app.get("/items/{item_id}")
def get_item_function(item_id: int):
    return {"item" : items.get(item_id, "Not found")}

#add an item
@app.post("/items/")
def add_item_function(item: Item):
    items[len(items)+1] = item.name
    return f"Added {items.name}"

#update an item
@app.put("/items/{item_id}")
def update_item_function(item_id:int, item:str):
    items[item_id] = item
    return {items[item_id]}
