from fastapi import Fasstapi
import random

app=FastAPI()

@app.get('/')
async def root():
    return{
        "root":"site",'data':0
    }