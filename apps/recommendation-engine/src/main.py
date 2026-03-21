"""
Recommendation Engine - Matar's Iced Americano
ML-powered suggestions for the perfect order
"""

from fastapi import FastAPI
from typing import List

app = FastAPI(
    title="Recommendation Engine",
    description="ML-powered suggestions for Matar's Iced Americano",
    version="0.3.0-alpha"
)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "recommendation-engine", "version": "0.3.0-alpha"}

@app.get("/recommendations/{customer_id}")
async def get_recommendations(customer_id: str) -> dict:
    """Get personalized recommendations for a customer"""
    return {
        "customer_id": customer_id,
        "recommendations": [
            {"item": "Matar's Iced Americano", "confidence": 0.95, "reason": "Your usual order"},
            {"item": "Oat Milk Upgrade", "confidence": 0.72, "reason": "Popular with similar customers"},
            {"item": "Vanilla Cold Brew", "confidence": 0.68, "reason": "Based on your taste profile"},
        ]
    }

@app.get("/recommendations/time-based")
async def time_based_recommendations() -> dict:
    """Get recommendations based on time of day"""
    return {
        "time": "morning",
        "recommendations": [
            {"item": "Matar's Iced Americano", "reason": "Morning caffeine boost"},
            {"item": "Breakfast Sandwich", "reason": "Pairs well with coffee"},
        ]
    }

@app.get("/recommendations/weather")
async def weather_recommendations(temp_celsius: float) -> dict:
    """Get recommendations based on weather"""
    if temp_celsius > 25:
        return {"suggestion": "Perfect day for an Iced Americano! ☀️"}
    else:
        return {"suggestion": "Maybe try our hot americano today? ☕"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
