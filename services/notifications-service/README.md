# Notifications Service 📱

Customer communications for Matar's Iced Americano.

## Overview

Channels:
- Push notifications (iOS/Android)
- SMS (Twilio)
- Email (SendGrid)

Use cases:
- "Your order is ready!"
- Promotional campaigns
- Loyalty rewards alerts
- Order confirmations

## Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Queue:** Celery + Redis

## Quick Start

```bash
cd services/notifications-service
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Team

Owned by **customers-team** - reach us at #customers on Slack.
