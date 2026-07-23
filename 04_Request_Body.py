from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Till here, we only saw the get method only, but we also have other methods like post, put, delete, patch etc. 

@app.get('/blog')
def intro():
    return {'message': 'Hello World'}

# so now let's see the post method, which is used to create a new resource in the database.

# As we know that get method is tested from the browser URL but post method can't 
# So, for it we can use swagger UI which is provided by FastAPI.

'''
Question : How can we create new resource in the database using post method in FastAPI? means how can we insert new data in the database using post method ..

Answer : When you need to send data from client to your API, you send it as Request Body. To declare the Request Body, we need to use Pydantic models.

--> Now, question arises that how??
'''

from pydantic import BaseModel # Step 1 : Import BaseModel from pydantic

class Blog(BaseModel): # Step 2 : Create a class which inherits from BaseModel
    title : str 
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(blog_request : Blog): # Step 3 : Create a function which takes the class as parameter
    return {"data" : f"Blog is created with title as {blog_request.title}"}


'''
Debugging means test the code by the system and check if it is working fine or not.

Question is HOW ??:

--> at the point of creating a new blog (return statement, here line 34), we can see that a faded red dot just before the line number so press it so it becomes a dark red dot, which means a breakpoint is set at that line.
--> Now, press ctrl + shift + p to open the debug window and then serach for debug:restart and click on it, so the debug window will open.
--> To show all the information related to this debugging, press ctrl + shift + d or go to same debug window and search for "View: Show Run and Debug" and click on it, so the debug window will open.
'''

# If we wish to run our code onto the another port just for the debugging purpose..
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)