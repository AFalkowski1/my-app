import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

DATA_FILE = os.environ.get('DATA_FILE', '/data/items.json')


def read_items():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def write_items(items):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f)


@app.route('/health')
def health():
    return jsonify({"status": "ok"})


@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(read_items())


@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.get_json()
    items = read_items()
    items.append(item)
    write_items(items)
    return jsonify(item), 201


@app.route('/api/stats')
def stats():
    return jsonify({"count": len(read_items())})