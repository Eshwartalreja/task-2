from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import Book
from schemas.index import BookSc

BookRouter = APIRouter()


@BookRouter.get("/")
async def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@BookRouter.get("/{id}")
async def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@BookRouter.post("/")
async def create_book(book: BookSc, db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@BookRouter.put("/{id}")
async def update_book(id: int, book: BookSc, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for attr, value in book.dict().items():
        setattr(db_book, attr, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@BookRouter.delete("/{id}")
async def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
