from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "hello, world!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# パスは順番に解決される
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


# 先に"/me"が定義されてるので、/meにアクセス時には劣後する
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# 文字列型、列挙型を継承したモデルを作成することで、特定の文字列しかパラメータとして受け付けないようにする
# また、これは/docsにも反映される
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    # クラスのメンバと比較できる
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    #
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# ファイル操作の例
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}