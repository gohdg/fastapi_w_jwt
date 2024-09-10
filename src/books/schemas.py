from pydantic import BaseModel


class Book(BaseModel):
    # pydantic model 정의
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    # pydantic model 정의
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
