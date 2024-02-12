from pydantic import BaseModel

class BookSc(BaseModel):
    book_id: int
    order_id: int
    isbn: str
    title: str
    author: str
