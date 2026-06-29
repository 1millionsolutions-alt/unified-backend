from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScenarioRequest(BaseModel):
    ticker: str
    outlook: str
    timeframe: str

@app.get("/")
def root():
    return {"status": "UNIFIED backend is running"}

@app.get("/analyze")
def analyze():
    return {"message": "Analyze endpoint working"}

@app.get("/portfolio")
def portfolio():
    return {"message": "Portfolio endpoint working"}

@app.get("/alerts")
def alerts():
    return {"message": "Alerts endpoint working"}

@app.post("/scenario")
def scenario(req: ScenarioRequest):
    return {
        "ticker": req.ticker,
        "outlook": req.outlook,
        "timeframe": req.timeframe,
        "message": "Scenario modeling endpoint working"
    }
