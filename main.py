import re
from xmlrpc.client import DateTime

from fastapi import FastAPI ,HTTPException
from entity.User import User
from entity.Color import Color, is_valid_color
from typing import Optional
from datetime import datetime
from entity.Week import Week

app = FastAPI()
db = {
    "1": User(name="Alice", age=25),
    "2": User(name="Bob", age=30)
}
db_post ={
    "1" :
    # comment
    {
        "1":"great",
        "2": "awsome"
    },
    "2":
    # comment
    {
        "3":"Thank you",
        "4" : "You should do more exercise a"
    }
}
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



#cau3
@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    return {"message": f"Multiply {num1} by {num2} = {num1 * num2}"}

#cau4
@app.get("/favorite_color/{color}")
async def multiply(color: str):
   try:
        format_param = color.lower()
        return {"message": f"your favorite color is {Color(format_param).name}"}
   except Exception as e:
       return {"message": "invalid color"}

#cau5
@app.get("/hello")
async def say_hello(name : Optional[str] = "world"):
    return {"message": f"Hello {name}"}

# cau 6
@app.get("/valid/{year}")
async def valid_year(year: int):
    if year not in range(1900, datetime.now().year+1):
        raise HTTPException(status_code=404, detail="invalid year")
    return {"message": f"valid year : {year}"}

#cau7
@app.get("/day_status/{year}/{moth}/{day}")
async def day_status(year: int, moth: int, day: int):
    day = datetime(year,moth,day).weekday()
    if day >= 5:
        return {"message": f"date is weekend : {Week(day).name}"}
    return {"message": f"date is weekday : {Week(day).name}"}
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

@app.put("/user/{id}")
async def get_user(id: str, user_edit:User):
    if id not in db:
        raise HTTPException(status_code=404, detail=f"Invalid user ID: {id}")
    user = db[id]
    user.name = user_edit.name
    user.age = user_edit.age
    return {"message":"edited successful"}  # FastAPI sẽ tự động convert thành JSON


@app.delete("/user/{id}")
async def get_user(id: str):
    if id not in db:
        raise HTTPException(status_code=404, detail=f"Invalid user ID: {id}")
    db.pop(id)
    return {"message":"deleted successful"}  # FastAPI sẽ tự động convert thành JSON


#cau10
@app.get("/v1/greeting/{name}")
async def greeting(name: str):
    return {"message": f"hello {name}"}  # FastAPI sẽ tự động convert thành JSON

@app.get("/v2/greeting/{name}")
async def greeting_multible_languages(name: str):
    multiple_languages = {
        "en": f"Hello {name}",
        "fr": f"Bonjour {name}",
        "vi": f"Xin chào {name}"
    }
    return {"message": multiple_languages}

#cau11
@app.get("/hello/{language_code}/{name}")
async def greeting(language_code,name: str):
    languages = {"en": f"Hello {name}",
                 "fr": f"Bonjour {name}",
                 "vi": f"Xin chào {name}"}
    if language_code not in languages:
        raise HTTPException(status_code=404, detail=f"Invalid language code: {language_code}")
    return {"message": f"{languages[language_code]} {name}"}

#cau12

@app.get("/posts/{post_id}/comments/{comment_id}")
async def post_comment(post_id: str, comment_id: str):
    if post_id not in db_post:
        raise HTTPException(status_code=404, detail=f"Invalid post ID: {post_id}")
    if comment_id not in db_post[post_id]:
        raise HTTPException(status_code=404, detail=f"Invalid comment ID: {comment_id}")
    return {"comment": f"{db_post[post_id][comment_id]}"}

#cau13
@app.get("/file/{file_path:path}")
async def get_file(file_path: str):
    return {"status": f"receive file successfully {file_path}"}