# Order API ☕

The core service handling customer orders at Matar's Iced Americano.

## Overview

The Order API manages:
- Cart creation and management
- Order placement and validation
- Order status tracking
- Integration with payment and inventory services

## Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Cache:** Redis
- **Message Queue:** RabbitMQ

## Quick Start

```bash
cd services/order-api
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders` | Create new order |
| GET | `/orders/{id}` | Get order details |
| PUT | `/orders/{id}/status` | Update order status |
| GET | `/orders/customer/{id}` | Get customer's orders |

## Environment Variables

```
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
PAYMENT_SERVICE_URL=http://payment-gateway:8080
INVENTORY_SERVICE_URL=http://inventory-service:8080
```

## Team

Owned by **orders-team** - reach us at #orders on Slack.
