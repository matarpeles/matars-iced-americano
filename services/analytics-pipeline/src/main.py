"""
Analytics Pipeline - Matar's Iced Americano
Data-driven decisions for better coffee
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "analytics-pipeline", "version": "1.5.0"})

@app.route('/metrics/sales/today')
def sales_today():
    return jsonify({
        "date": "2024-03-21",
        "total_orders": 1247,
        "total_revenue": 5612.50,
        "avg_order_value": 4.50,
        "top_item": "Matar's Iced Americano"
    })

@app.route('/metrics/popular-items')
def popular_items():
    return jsonify({
        "items": [
            {"name": "Matar's Iced Americano", "orders": 523, "percentage": 42},
            {"name": "Cold Brew", "orders": 234, "percentage": 19},
            {"name": "Iced Latte", "orders": 189, "percentage": 15},
        ]
    })

@app.route('/metrics/peak-hours')
def peak_hours():
    return jsonify({
        "peak_hours": ["8:00-9:00", "12:00-13:00", "15:00-16:00"],
        "busiest_day": "Monday"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
