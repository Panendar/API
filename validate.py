from fastapi import FastAPI
from pydantic import BaseModel, Field, ValidationError, field_validator, EmailStr
from datetime import datetime
import re

app = FastAPI()

# class TaskValidation(BaseModel):
#     title:str = Field(...,min_length=3, max_length=50)   # the ... means its a required field
#     description: str =""    # optional field with default empty string
#     priority: int =Field(1,ge=1,le=5)   # optional if not set the default value is 1
#     due_date: datetime |None

#     @field_validator('due_date')
#     @classmethod
#     def check_due_date(cls, v):    # in pydantic V2 we use the field_validator decorator 
#         if v and v < datetime.now():           # we are getting the value of due_date in v from class we have created 
#             raise ValueError("due_date must be in the future")
#         return v
    
# basic_check = TaskValidation(
#     title="Complete assignment",
#     description="Finish the FastAPI assignment by tomorrow",
#     priority=3,
#     due_date=datetime(2024, 12, 31)
# )
# print(basic_check)


# class userRegistration(BaseModel):
#     username:str =Field(...,min_length=5, max_length=25)
#     email: EmailStr
#     password: str = Field(...,min_length=8, max_length=15)
#     age:int = Field(...,ge=13, le=120)
#     is_active: bool = Field(default=True)

    
#     @field_validator('password')
#     @classmethod
#     def valid_password(cls,v):
#         pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'
#         if not re.match(pattern, v):
#             raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
#         return v
    
# basic_check = userRegistration(
#     username="testuser",
#     email="panennkwjsnqiuhqnx@gmail.com",
#     password="password1!",
#     age=25)

# print(basic_check)

# @app.post("/register")
# def register_user(user: userRegistration):
#     return {"message": "User registered successfully", "user": user}


class Product(BaseModel):
    name: str = Field(...,min_length=5, max_length=150)
    price:float= Field(...,gt=0, le=100000)
    in_stock:int =Field(0, ge=0)
    category: str

    @field_validator('category')
    @classmethod
    def valid_category(clas,v):
        allowed = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
        if v not in allowed:
            raise ValueError(f"Category must be one of {allowed}")
        return v
    @field_validator('name')
    @classmethod
    def name_must_not_contain_spam(cls, v):
        spam_words = ['spam', 'fake_money', 'buy now', 'click here', 'free money']
        if any(word in v.lower() for word in spam_words):
            raise ValueError("Product name contains spam words.")
        return v
    

check = Product(
    name="Smartphone",
    price=699.99,
    in_stock=50,
    category="Electronics"
)
wrong_check = Product(
    name="Buy now fake_money",
    price=699.99,
    in_stock=50,
    category="apple"
)
print(check)
print(wrong_check)