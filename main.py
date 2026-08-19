from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from models import TemperatureResponse, RiskLevel

app = FastAPI()

known_locations = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437},
    "Chicago": {"lat": 41.8781, "lon": -87.6298},
    "Houston": {"lat": 29.7604, "lon": -95.3698},
    "Phoenix": {"lat": 33.4484, "lon": -112.0740},
}


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")   

@app.get("/risk/{location}")
async def get_risk_level(location: str) -> TemperatureResponse:
    if location not in known_locations:
        raise HTTPException(status_code=404, detail="Location not found")

    simulated_temperatures = {
        "New York": 30.0,
        "Los Angeles": 25.0,
        "Chicago": 15.0,
        "Houston": 35.0,
        "Phoenix": 40.0,
    }

    temperature = simulated_temperatures.get(location, 20.0)  # Default to 20.0 if location not found
    if temperature < 20:
        risk_level = RiskLevel.LOW
    elif temperature < 30:
        risk_level = RiskLevel.MODERATE
    elif temperature < 40:
        risk_level = RiskLevel.HIGH
    else:
        risk_level = RiskLevel.EXTREME

    return TemperatureResponse(location=location, temperature=temperature, risk_level=risk_level)

