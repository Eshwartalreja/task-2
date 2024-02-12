# from fastapi import APIRouter
# from config.db import conn
# from models.index import Customer
# from schemas.index import CustomerSc
# CustomerRouter  = APIRouter()

# @CustomerRouter.get("/")
# async def read_data():
#     return conn.execute(Customer.select()).fetchall()

# @CustomerRouter.get("/{id}")
# async def read_data(id:int):
#     return conn.execute(Customer.select().where(Customer.c.id == id)).fetchall()

# @CustomerRouter.post("/")
# async def write_data(customers :CustomerSc):
#     conn.execute(Customer.insert().values(
#         name =customers.name,
#         email =customers.email,
#         password=customers.password

#     ))
#     return conn.execute(Customer.select()).fetchall()

# @CustomerRouter.put("/{id}")
# async def update_data(id:int,customers:CustomerSc):
#     conn.execute(Customer.update().values(
#         name =customers.name,
#         email =customers.email,
#         password=customers.password
#     ).where(Customer.c.id == id))
    
#     return conn.execute(Customer.select()).fetchall()

# @CustomerRouter.delete("/{id}")
# async def delete_data(id:int):
#     conn.execute(Customer.delete().where(Customer.c.id == id))
#     return conn.execute(Customer.select()).fetchall()