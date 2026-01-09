# from fastapi import FastAPI

# #create Instance object
# app = FastAPI()

# # DEfine routes
# @app.get("/")   # decorator wraps the function with the API functionality tells this function handles get request to this path
# # we can use other HTTP methods like Get- retrieve the data, Post- create data(new data), Put- update data, Delete - delete data

# def read_root():
#     return {"message" : "Hello, World!"}


# from fastapi import FastAPI

# app = FastAPI(title="MY FIRST API", version="1.0")

# @app.get("/")
# def read_root():
#     return {"Greeting": "Welcome to my API!..."}

# @app.get("/items")
# def items_list():
#     return {"items": ["item1", "item2", "item3"]}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q:str = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/health")
# def health_check():
#     return {"status": "OK"}


# pydantic the validation, parsing, clear error messages, converts data types automatically(e.g., strings to integers)
    # ex: def create_user(data):
    #    # Manual validation nightmare
    #    if not isinstance(data.get('age'), int):
    #        raise ValueError("Age must be an integer")
    #    if data['age'] < 0 or data['age'] > 150:
    #        raise ValueError("Age must be between 0 and 150")
    #    if not isinstance(data.get('email'), str) or '@' not in data['email']:
    #        raise ValueError("Invalid email format")
    #    if not isinstance(data.get('is_active'), bool):
    #        raise ValueError("is_active must be a boolean")
    
    #    # Finally create the user...
    #    return User(data['age'], data['email'], data['is_active'])

# you define your data structure once using Python’s type annotation syntax, and Pydantic handles all the validation automatically:


# from fastapi import FastAPI
# from pydantic import BaseModel
# import logging
# from datetime import datetime

# app = FastAPI()
# logging.basicConfig(level=logging.INFO)

# class Item(BaseModel):     # in base model we define the structure of the data we expect/ get from user
#     name: str
#     description : str = None

# class Response(BaseModel):
#     id: int
#     name: str
#     price: float
#     created_at: str

# @app.post("/items")
# def create_item(item: Item):
#     logging.info(f"1. Received request for item: {item.name}")

#     #Validation already done by FastAPI/Pydantic
#     logging.info("2. Validation successful")

#     #Processing the item
#     response = {
#         "id" : 1,
#         "name" : "{item.name}",
#         "price" : 9.99,
#         "created_at" : datetime.now().isoformat()
#     }

#     # Response
#     logging.info("3. Sending response")
#     return response




# Fast API has the asyc support it can handle multiple requests concurrently

# from fastapi import FastAPI
# import asyncio

# app = FastAPI()

# @app.get("/slow-task")
# async def slow_task():
#     await asyncio.sleep(2)  # Simulate a slow task that takes 2 seconds
#     return {"message": "Task completed!"}


# basic FASTAPI Greeting function
from fastapi import FastAPI
app = FastAPI()
from datetime import datetime

# @app.get("/greeting/{name}")
# def greet_name(name: str):
#     return {
#         "message": f"Hello, {name}! Welcome to our API.",
#         "timestamp": datetime.now().isoformat()
#         }



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()
# class UserResponse(BaseModel):
#     ID: int
#     name: str
# @app.get("/users/{user_id}")
# def get_user(user_id: int) -> UserResponse:
#     return UserResponse(ID=user_id, name="John")



# Path Parameters: Part of the URL path itself
# Example: /users/123 → 123 is the path param


# Query Parameters: Added after a ? in the URL
# Example: /users?age=25&city=NYC → age and city are query params

# get all the electronic devices from products under 20000
# /products?category=electronic&max_price=20000

@app.get("/")
def root():
    return {"message": "Welcome to the Greeting API!"}
@app.get("/{name}")
def greeting(name: str, q: str = None):
    response = {
        "message": f"Hello, {name}!\nWelcome to our API.",
        "timestamp": datetime.now().isoformat(),
        "language": q if q else "english"
    }
    return response
