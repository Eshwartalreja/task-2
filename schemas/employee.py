from pydantic import BaseModel
    
class EmployeeSc(BaseModel):
    name:str
    contact:str 
    jobTitle:str
    workSchedule:str 