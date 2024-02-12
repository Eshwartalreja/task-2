from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import Employee
from schemas.index import EmployeeSc

EmployeeRouter = APIRouter()


@EmployeeRouter.get("/", response_model=list[EmployeeSc])
async def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@EmployeeRouter.get("/{id}", response_model=EmployeeSc)
async def get_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@EmployeeRouter.post("/", response_model=EmployeeSc)
async def create_employee(employee: EmployeeSc, db: Session = Depends(get_db)):
    print(employee, 'checking')
    try:
        new_employee = Employee(
            name=employee.name,
            contact=employee.contact,
            jobTitle=employee.jobTitle,
            workSchedule=employee.workSchedule
        )
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
    except Exception as e:
        print('error',e)
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to create employee") from e
    return new_employee


@EmployeeRouter.put("/{id}", response_model=EmployeeSc)
async def update_employee(id: int, employee: EmployeeSc, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for attr, value in employee.dict().items():
        setattr(db_employee, attr, value)
    try:
        db.commit()
        db.refresh(db_employee)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to update employee") from e
    return db_employee

@EmployeeRouter.delete("/{id}")
async def delete_employee(id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    try:
        db.delete(employee)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to delete employee") from e
    return {"message": "Employee deleted successfully"}
