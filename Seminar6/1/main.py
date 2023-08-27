import uvicorn
import users_1
import posts_1
from fastapi import FastAPI
from database import *
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup():
    await database.connect()
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
    
app.include_router(users_1.router, tags=["users"])
app.include_router(posts_1.router, tags=["posts"])

if __name__ == '__main__':
    uvicorn.run(
    "main:app",
    # host="127.0.0.1",
    # port=8000,
    reload=True
    )