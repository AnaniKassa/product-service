import os
from flask import Flask, jsonify
from flask_cors import CORS

# Flask app
app = Flask(__name__)

# Enable CORS for /products (allow all origins)
CORS(app, resources={r"/products": {"origins": "*"}})

# Example products data
products_data = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 500},
    {"id": 4, "name": "SmartGlasses", "price": 700}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products_data)

# Azure will inject PORT, so must listen on 0.0.0.0:<PORT>
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3030))  # Azure defaults to PORT env
    app.run(host="0.0.0.0", port=port)
