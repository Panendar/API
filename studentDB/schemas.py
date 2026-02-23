from pydantic import BaseModel

class StudentResponse(BaseModel):
    ID:int
    NAME:str
    AGE:int
    MOBILE_NO:str
    EMAIL:str

class StudentCreate(BaseModel):
    NAME:str
    AGE:int
    MOBILE_NO:str
    EMAIL:str