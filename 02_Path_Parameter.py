
from fastapi import FastAPI

app = FastAPI()

# function to fetch one single blog
# @app.get('/blog')
# def show_blog():    
#     return {"data": "Blog List"}

# function to fetch the blog with id
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

# Solution of confusion : which part we wanto run first that must be on top of confusing part. 

# To make these all the validation we have one library called Pydantic.
