from fastapi import FastAPI
from pydantic import BaseModel
from ratingAlgorithm import TimeDecayReputation

app = FastAPI()
reputation_system = TimeDecayReputation()

class Transaction(BaseModel):
    order_value: float
    return_days: int

@app.post("/update_score/")
def update_score(transaction: Transaction):
    new_score = reputation_system.update_score(transaction.order_value, transaction.return_days)
    return {"updated_rating": round(new_score, 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
