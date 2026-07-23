from fastapi import FastAPI 

app = FastAPI()  

@app.get('/')
def intro():
    return "Hello, I am learning FastAPI!"

@app.get('/blog')
def index(limit, published : bool):
    return published
    if published :
        return {'data' : f'{limit} published blogs from the database'}       
    else :
        return {'data' : f'{limit} blogs from the database'}   
        
# To check this into the browser,
# you can use the following URL: http://127.0.0.1:8000/blog?limit=50&published=false

# For the default values we can give it like this :
# def index(limit=10, published : bool = True):

# Note : If you provide one parameter as default then you have to provide all the parameters as default.

'''
Question arise that suppose any parameter which we not want to make default then ?
def index(limit=10, published : bool = True, sort : Optional[str] = None):

This might give you an error because Optional is not included in to the FastAPI so we need to import it from typing module. So we can do it like this : from typing import Optional

To check this into the browser,
you can use the following URL: http://127.0.0.1:8000/blog?sort=latest
'''



'''
MOST IMPORTANT : How can we identify that what is query parameter and what is path parameter ?

--------------------- In the CODE ------------------------
--> If we not give parameter in the path then it is query parameter.
--> If we give the parameter in the path and also used in the fuction parametersthen it is path parameter.

----------------- In the browser URL ---------------------
--> If we provide the parameter in the path then it is path parameter 
--> If we provide the parameter after the question mark then it is query parameter .
'''


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data' : f'blog with id {id} and limit {limit}'}

'''
Quick Quiz : What is 'id' and 'limit' here in the above function ?
Answer : 
--> 'id' is path parameter because 'id' is provided in the path as well as in the function parameter
--> 'limit' is query parameter because 'limit' is provided only in the function parameter.
'''