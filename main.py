from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from routers import users  , auth
from database import get_db
from database import Base  , engine
import models

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

Base.metadata.create_all(bind = engine)
@app.get('/')
def home():
    return {"message": "Hello, World!"}


if __name__ =='__main__':
    uvicorn.run('main:app', host='localhost', port=9000 , reload = True)
