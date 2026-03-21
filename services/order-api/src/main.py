"""
Order API - Matar's Iced Americano
The heartbeat of every iced americano served.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

app = FastAPI(
    title="Order API",
    description="Core service handling customer orders at Matar's Iced Americano",
    version="3.2.1"
)

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderItem(BaseModel):
    item_id: str
    name: str
    quantity: int
    price: float
    customizations: Optional[List[str]] = []

class Order(BaseModel):
    id: Optional[str] = None
    customer_id: str
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    total: float
    created_at: Optional[datetime] = None
    store_id: str

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "order-api", "version": "3.2.1"}

@app.post("/orders")
async def create_order(order: Order):
    """Create a new order for an iced americano (or other drinks)"""
    order.id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    order.created_at = datetime.now()
    return {"message": "Order created", "order": order}

@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    """Get order details by ID"""
    return {
        "id": order_id,
        "customer_id": "CUST-001",
        "items": [{"name": "Iced Americano", "quantity": 1, "price": 4.50}],
        "status": "preparing",
        "total": 4.50
    }

@app.put("/orders/{order_id}/status")
async def update_order_status(order_id: str, status: OrderStatus):
    """Update order status"""
    return {"message": f"Order {order_id} updated to {status}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
