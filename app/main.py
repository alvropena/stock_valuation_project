from fastapi import FastAPI
from app.controllers import run_valuation

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Valuation API"}

@app.get("/valuation/{ticker}")
def stock_valuation(ticker: str):
    return run_valuation(ticker)
