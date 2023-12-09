from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


affiliate_db = {}
commission_rate = 0.1  


class Affiliate(BaseModel):
    id: int
    name: str
    email: str


@app.get("/affiliates/{affiliate_id}")
async def get_affiliate(affiliate_id: int):
    if affiliate_id not in affiliate_db:
        return {"Err": "Affiliate not found"}
    return affiliate_db[affiliate_id]


@app.post("/affiliates/create/")
async def create_affiliate(affiliate: Affiliate):
    affiliate_db[affiliate.id] = affiliate.dict()
    return {"message": "Affiliate created successfully"}


@app.get("/calculate-commission/{affiliate_id}/{sales_amount}")
async def calculate_commission(affiliate_id: int, sales_amount: float):
    if affiliate_id not in affiliate_db:
        return {"message": "Affiliate not found"}

    commission = sales_amount * commission_rate
    return {"affiliate_id": affiliate_id, "commission_amount": commission}
