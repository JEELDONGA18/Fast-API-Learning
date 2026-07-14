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

# function to fetch one single blog
# @app.get('/blog')
# def show_blog():    
#     return {"data": "Blog List"}

# @app.get('/blog/{id}')
# def show_blog(id):    
#     return {"data": id}
# for the dynamic path we need to use the curly braces {} and inside that we can give any name for the variable. 
# that variable name is given at 3 places :
# 1. Inside the curly braces {} in the path 
# 2. Inside the function name as a parameter
# 3. Inside the return statement to return the value of that variable.

@app.get('/blog/{id}/comments')
def show_blog(id):    
    return {"data": {"1","2","3"}}


# To restrict the id is without number like string or float or something we can do like this :
@app.get('/blog/{id}')
def show_blog(id: int):    # This ": int " restricts the id to be only integer. If we give any other type of value it will give an error.
    return {"data": id}

# Let's make confusion 
@app.get('/blog/unpublished')
def show_blog():  
    return {"data": "All Unpublished Blogs.."}

# By running this if above function is present then it wll give an error because the path is same as the above function.
# like /blog/... so it looks that unpublished is string and it match with id but it must be in int but here unpublished is string.
# ****** Rule : Fastapi is running from top to bottom 


# To make these all the validation we have one library called Pydantic.
