from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"
# 아래 옵션은 docs에 표시되는 내용이당
app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])

# uvicorn src:app --reload
