from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


# 🔥 Replace with your MongoDB Atlas URL
client = MongoClient("mongodb+srv://demofor26:vfuHPh2i617itRKF@project-data.4nfr4xv.mongodb.net/productDB?retryWrites=true&w=majority")

db = client["project-data"]
collection = db["products"]

@app.route("/")
def home():
    return render_template("index.html")

# ➕ Add Product
@app.route("/add", methods=["POST"])
def add_product():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Product added"})

# 🔍 Search Product
@app.route("/search/<name>", methods=["GET"])
def search_product(name):
    product = collection.find_one({"name": name})

    if product:
        product["_id"] = str(product["_id"])
        return jsonify(product)
    else:
        return jsonify(None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)