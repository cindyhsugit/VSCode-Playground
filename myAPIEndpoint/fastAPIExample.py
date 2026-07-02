from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str

items = {1: Item(name="Apple"), 2:Item(name="Banana")}

#retrieve an item
@app.get("/items/{item_id}")
def get_item_function(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="out of index error")
    return {"item" : items.get(item_id, "Not found")}

#add an item
@app.post("/items/")
def add_item_function(item: Item):
    items[len(items)+1] = item.name
    return f"Added {items.name}"

#update an item
@app.put("/items/{item_id}")
def update_item_function(item_id:int, item:str):
    if item_id not in items:
        raise HTTPException(status_code= 404, detail="update fail")
    items[item_id] = item
    return {items[item_id]}

#only execeute directly
if __name__ == "__main__":
    print(f"You are running  {__file__}")
