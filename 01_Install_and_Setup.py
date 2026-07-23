from fastapi import FastAPI # First : Import FastAPI

app = FastAPI()  # Second : Make Instance of FastAPI

@app.get('/')
def index():
    return "Hello, I am learning FastAPI!"  # Third : Define a function that returns a string

# by Running till here , it will generate an error because we not used app till now.

# Fourth : to run till here go to terminal and move inside the venv and then type : uvicorn 01_Install_and_Setup:app --reload
# You will get {"detail":"Not Found"} at http://127.0.0.1:8000/ and 
# also in the terminal : INFO:     127.0.0.1:53373 - "GET / HTTP/1.1" 404 Not Found
#                        INFO:     127.0.0.1:53373 - "GET /favicon.ico HTTP/1.1" 404 Not Found

# so to fix this error we need to put the function inside a path for it to work. (for it see line 5)

@app.get('/about')
def index():
    return {'My Self': {
        "Name " : "Jeel Donga"
    }} 
# NOTE : If you give same name of the function like the index that dosen't cause any error because the function name is not important but the path is important. So if you give same name of the function it will work fine. But this is not good practice. 
    
# @app.get('/about')
# def about():
#     return {'My Self': {
#         "Name " : "Jeel Donga"
#     }} 

# Introduction with syntax : 
# @app --> Path operation decorator that tells FastAPI that this function is a path operation
# .get() --> Operation that tells FastAPI that this function is a GET request
# ('/..') --> Path that tells FastAPI that this function is a path operation for the given path
# def about():  --> Path decorator function that tells FastAPI that this function is a path operation for the given path