from locust import HttpUser, task, between
from faker import Faker
from uuid import uuid4
import random

fake = Faker()

def make_email(first_name:str, last_name:str, company:str = "jbdc", extension:str = 'org') -> str:
    """Generate an email address from the first name and last name."""
    return f"{first_name.lower()}.{last_name.lower()}@{company}.{extension}"
class UserBehavior(HttpUser):
    wait_time = between(1, 2.5)
    orders = []

    @task(1)
    def create_user(self):
        """Send a POST request to the /create_user endpoint."""
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = make_email(first_name, last_name)
        self.client.post("/create_user", json={
            "user_id": str(uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": fake.password(),
            "date_of_birth": fake.date_of_birth().isoformat()
        })

    @task(2)
    def add_product(self):
        """Send a POST request to the /add_product endpoint."""
        self.client.post("/add_product", json={
            "product_id": str(uuid4()),
            "name": fake.word(),
            "category": fake.word(),
            "price": round(random.uniform(5.0, 100.0), 2),
            "stock": random.randint(0, 100)
        })

    @task(3)
    def add_order(self) -> None:
        """Send a POST request to the /add_order endpoint."""
        user_id = str(uuid4())
        product_id = str(uuid4())
        quantity = random.randint(1, 5)
        total_price = round(random.uniform(5.0, 500.0), 2)
        order_date = fake.date_this_year().isoformat()
        shipping_address = fake.address()
        payment_method = fake.credit_card_provider()
        payment_status = "Completed"
        self.orders.append({
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price,
            "order_date": order_date,
            "shipping_address": shipping_address,
            "payment_method": payment_method,
            "payment_status": payment_status
        })
        self.client.post("/add_order", json={
            "order_id": str(uuid4()),
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price,
            "order_date": order_date,
            "shipping_address": shipping_address,
            "payment_method": payment_method,
            "payment_status": payment_status
        })

    @task(4)
    def update_order(self):
        """Send a PUT request to the /update_order endpoint."""
        self.client.put("/update_order/1", json={
            "quantity": 1,
            "total_price": 100.0,
            "order_date": "2022-01-01",
            "shipping_address": "Address 1",
            "payment_method": "Credit Card",
            "payment_status": "Paid"
        })

    @task(5)
    def get_order_status(self):
        """Send a GET request to the /order_status endpoint."""
        self.client.get("/order_status/1")
    
    @task(6)
    def get_products(self):
        """Send a GET request to the /products endpoint."""
        self.client.get("/products")

    @task(7)
    def get_users(self):
        """Send a GET request to the /users endpoint."""
        self.client.get("/users")
    
    @task(8)
    def get_orders(self):
        """Send a GET request to the /orders endpoint."""
        self.client.get("/orders")