import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env (like dotenv in Rust)
load_dotenv()

app = Flask(__name__)

# Enable CORS (allow all origins, GET only)
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

# Example products data
products_data = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 500}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products_data)

if __name__ == "__main__":
    # Get port from env or default to 3030
    port = int(os.getenv("PORT", 3030))
    app.run(host="0.0.0.0", port=port)
