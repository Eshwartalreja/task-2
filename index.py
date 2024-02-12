from fastapi import FastAPI
from routes.index import BookRouter,EmployeeRouter

app = FastAPI()


# app.include_router(CustomerRouter,prefix='/customer')
app.include_router(EmployeeRouter,prefix='/employee')
app.include_router(BookRouter,prefix='/book')
