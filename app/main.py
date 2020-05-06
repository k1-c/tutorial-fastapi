from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """
    Request Bodyを使いたい場合、Pydanticを利用する。
    Pydanticに定義された型・Bodyが要求される。
    If its not required, declare default value.
    """
    return item


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
    # Putを利用する場合
    # return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    """
    クエリパラメータとPutを利用する
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result