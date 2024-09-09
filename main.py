from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}


@app.get('/greet')
# query parameter
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


# @app.get('/greet/{name}')
# # path parmeter & query parameter
# async def greet_name(name: str, age:int) -> dict:
#     return {"message": f"Hello {name}", "age": age}

class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post('/create_book')
# body data가 default
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@app.get('/get_headers',)
# header 데이터 접근을 위해서는 FastAPI의 Header class 필요
# header data 접근 방법
async def get_headers(
    username: str = Header(None),
    password: str = Header(None),
    credential: str = Header(None)
):
    request_headers = {}

    request_headers["username"] = username
    request_headers["password"] = password
    request_headers["credential"] = credential

    return request_headers
