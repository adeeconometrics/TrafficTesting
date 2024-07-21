from faker import Faker
import random
from sqlite3 import connect
from pathlib import Path

fake = Faker()

def make_users(count: int, db_instance:str | Path) -> None:
    """Generate mock data for users"""
    with connect(db_instance) as conn:
        cursor = conn.cursor()
        cursor.execute('BEGIN')
        for _ in range(count):
            user = {
                "user_id": fake.uuid4(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "password": fake.password(),
                "date_of_birth": fake.date_of_birth().isoformat()
            }
            cursor.execute('''INSERT INTO users (user_id, first_name, last_name, email, password, date_of_birth)
                              VALUES (:user_id, :first_name, :last_name, :email, :password, :date_of_birth)''', user)
        cursor.execute('COMMIT')

def make_orders(count:int, db_instance: str | Path) -> None:
    """Generate mock data for orders"""
    with connect(db_instance) as conn:
        cursor = conn.cursor()
        cursor.execute('BEGIN')
        for _ in range(count):
            order = {
                "order_id": fake.uuid4(),
                "user_id": fake.uuid4(),
                "product_id": fake.uuid4(),
                "quantity": random.randint(1, 5),
                "total_price": round(random.uniform(5.0, 500.0), 2),
                "order_date": fake.date_this_year().isoformat(),
                "shipping_address": fake.address(),
                "payment_method": fake.credit_card_provider(),
                "payment_status": "Completed"
            }
            cursor.execute('''INSERT INTO orders (order_id, user_id, product_id, quantity, total_price, order_date, shipping_address, payment_method, payment_status)
                              VALUES (:order_id, :user_id, :product_id, :quantity, :total_price, :order_date, :shipping_address, :payment_method, :payment_status)''', order)
        cursor.execute('COMMIT')


def make_products(count:int, db_instance: str | Path) -> None:
    """Generate mock data for products"""
    with connect(db_instance) as conn:
        cursor = conn.cursor()
        cursor.execute('BEGIN')
        for _ in range(count):
            product = {
                "product_id": fake.uuid4(),
                "name": fake.word(),
                "category": fake.word(),
                "price": round(random.uniform(5.0, 100.0), 2),
                "stock": random.randint(0, 100)
            }
            cursor.execute('''INSERT INTO products (product_id, name, category, price, stock)
                              VALUES (:product_id, :name, :category, :price, :stock)''', product)
        cursor.execute('COMMIT')
        

if __name__ == "__main__":
    make_users(10, "database.db")
    # make_products(10, "database.db")
    # make_orders(10, "database.db")