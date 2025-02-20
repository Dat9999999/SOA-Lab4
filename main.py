import re

from fastapi import FastAPI ,HTTPException
from entity.User import User

app = FastAPI()
db = {
    "1": User(name="Alice", age=25),
    "2": User(name="Bob", age=30)
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



#cau 8
@app.get("/product/{product_id}")
async def get_product(product_id: str):
    regex = r"^[a-zA-Z]{3}-\d{3}$"
    if not (re.match(regex, product_id)):
        return {"message": f"invalid product id : {product_id}"}
    else:
        return {"message": f"show product id {product_id}"}

#cau 9
@app.get("/user/{id}")
async def get_user(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail=f"Invalid user ID: {id}")

    return {"user": db[id]}  # FastAPI sẽ tự động convert thành JSON




