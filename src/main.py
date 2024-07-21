
from flask import Flask, request, jsonify
from sqlite3 import connect

from typing import Dict, Any

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login() -> Dict[str, Any]:
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

    if user:
        return jsonify({"status": "success", "message": "Logged in successfully"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid credentials"}), 401


@app.route('/order_status/<order_id>', methods=['GET'])
def get_order_status(order_id) -> Dict[str, Any]:
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        order = cursor.fetchone()

    if order:
        return jsonify({"status": "success", "order": order}), 200
    else:
        return jsonify({"status": "failure", "message": "Order not found"}), 404


@app.route('/products', methods=['GET'])
def get_products() -> Dict[str, Any]:
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

    return jsonify({"status": "success", "products": products}), 200

@app.route('/users', methods=['GET'])
def get_users() -> Dict[str, Any]:
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    return jsonify({"status": "success", "users": users}), 200

@app.route('/orders', methods=['GET'])
def get_orders() -> Dict[str, Any]:
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

    return jsonify({"status": "success", "orders": orders}), 200

@app.route('/create_user', methods=['POST'])
def create_user() -> Dict[str, Any]:
    data = request.get_json()
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (user_id, first_name, last_name, email, password, date_of_birth) VALUES (?, ?, ?, ?, ?, ?)",
                       (data["user_id"], data["first_name"], data["last_name"], data["email"], data["password"], data["date_of_birth"]))
        conn.commit()
    return jsonify({"status": "success", "message": "User created successfully"}), 201


@app.route('/add_product', methods=['POST'])
def add_product() -> Dict[str, Any]:
    data = request.get_json()
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (product_id, name, category, price, stock) VALUES (?, ?, ?, ?, ?)",
                       (data["product_id"], data["name"], data["category"], data["price"], data["stock"]))
        conn.commit()
    return jsonify({"status": "success", "message": "Product added successfully"}), 201


@app.route('/update_order/<order_id>', methods=['PUT'])
def update_order(order_id: str) -> Dict[str, Any]:
    data = request.get_json()
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET quantity = ?, total_price = ?, order_date = ?, shipping_address = ?, payment_method = ?, payment_status = ? WHERE order_id = ?",
                       (data["quantity"], data["total_price"], data["order_date"], data["shipping_address"], data["payment_method"], data["payment_status"], order_id))
        conn.commit()
    return jsonify({"status": "success", "message": "Order updated successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
