from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    jobTitle = Column(String)
    workSchedule = Column(String)
    
    
    sales = relationship('Sales', back_populates='employee')