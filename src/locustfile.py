from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def create_user(self):
        """Send a POST request to the /create_user endpoint."""
        self.client.post("/create_user", json={
            "user_id": "1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "password": "password",
            "date_of_birth": "2000-01-01"
        })

    @task(2)
    def add_product(self):
        """Send a POST request to the /add_product endpoint."""
        self.client.post("/add_product", json={
            "product_id": "1",
            "name": "Product 1",
            "category": "Category 1",
            "price": 100.0,
            "stock": 10
        })

    @task(3)
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