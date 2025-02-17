from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ratingAlgorithm import TimeDecayReputation

app = FastAPI()

# Define request body schema
class Order(BaseModel):
    order_value: int
    return_days: int

class OrdersRequest(BaseModel):
    transactions: List[Order]

# Initialize reputation system
reputation_system = TimeDecayReputation()

@app.post("/update-score")
def update_score(data: OrdersRequest):
    scores = []
    for order in data.transactions:
        new_score = reputation_system.update_score(order.order_value, order.return_days)
        scores.append({"order_value": order.order_value, "return_days": order.return_days, "updated_score": new_score})
    
    return {"updated_scores": scores}
