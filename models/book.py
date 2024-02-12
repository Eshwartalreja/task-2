from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)  
    order_id = Column(Integer)  
    isbn = Column(String)  
    title = Column(String)  
    author = Column(String)  
    
    
    sales = relationship('Sales', back_populates='book')
