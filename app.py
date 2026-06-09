from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.get_json()
    items.append(item)
    return jsonify(item), 201

@app.route('/api/stats')
def stats():
    return jsonify({"count": len(items)})