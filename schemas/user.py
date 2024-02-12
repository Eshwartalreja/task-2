from pydantic import BaseModel
    
class CustomerSc(BaseModel):
 
    name:str
    email:str 
    password:str 
    
