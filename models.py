from pydantic import BaseModel
from enum import Enum

class RiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    EXTREME = "extreme"

class TemperatureResponse(BaseModel):
    location: str
    temperature: float
    risk_level: RiskLevel