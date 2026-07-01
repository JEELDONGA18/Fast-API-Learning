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