from fastapi import fastapi
import random

app=FastAPI()

@app.get('/')
async def root():