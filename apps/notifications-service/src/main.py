"""
Notifications Service - Matar's Iced Americano
Keeping customers in the loop
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

app = FastAPI(
    title="Notifications Service",
    description="Customer communications for Matar's Iced Americano",
    version="2.1.0"
)

class Channel(str, Enum):
    SMS = "sms"
    EMAIL = "email"
    PUSH = "push"

class Notification(BaseModel):
    customer_id: str
    channel: Channel
    template: str
    data: Optional[dict] = {}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "notifications-service", "version": "2.1.0"}

@app.post("/notify")
async def send_notification(notification: Notification):
    return {
        "message": "Notification queued",
        "channel": notification.channel,
        "customer_id": notification.customer_id
    }

@app.post("/notify/order-ready")
async def order_ready(order_id: str, customer_id: str):
    return {
        "message": "Order ready notification sent",
        "order_id": order_id,
        "channels": ["push", "sms"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
