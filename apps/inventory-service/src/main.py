"""
Inventory Service - Matar's Iced Americano
Never run out of what makes the perfect iced americano
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {
    "coffee-beans-ethiopian": {"name": "Ethiopian Yirgacheffe", "quantity": 50, "unit": "kg", "low_threshold": 10},
    "coffee-beans-colombian": {"name": "Colombian Supremo", "quantity": 75, "unit": "kg", "low_threshold": 15},
    "oat-milk": {"name": "Oat Milk", "quantity": 200, "unit": "liters", "low_threshold": 50},
    "whole-milk": {"name": "Whole Milk", "quantity": 150, "unit": "liters", "low_threshold": 40},
    "cups-large": {"name": "Large Cups (16oz)", "quantity": 5000, "unit": "units", "low_threshold": 1000},
}

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "inventory-service", "version": "2.3.0"})

@app.route('/inventory')
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<item_id>')
def get_item(item_id):
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({item_id: inventory[item_id]})

@app.route('/inventory/<item_id>/adjust', methods=['POST'])
def adjust_inventory(item_id):
    if item_id not in inventory:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.json
    adjustment = data.get('adjustment', 0)
    inventory[item_id]['quantity'] += adjustment
    
    return jsonify({"message": "Inventory adjusted", "new_quantity": inventory[item_id]['quantity']})

@app.route('/inventory/low-stock')
def low_stock():
    low = {k: v for k, v in inventory.items() if v['quantity'] <= v['low_threshold']}
    return jsonify(low)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
