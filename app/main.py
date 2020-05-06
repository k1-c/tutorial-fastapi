from fastapi import FastAPI, Query
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    """
    Queryを使ってデフォルト値とカスタムバリデーションを加える
    ex. ３文字以上５０文字以下
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
