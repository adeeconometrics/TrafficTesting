from faker import Faker
from locust import HttpUser, task, between
from random import randint

fake = Faker()

class UserBehaviorAsp(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def get_order(self) -> None:
        self.client.get("api/Order")

    @task(2)
    def post_order(self) -> None:
        self.client.post("api/Order", json={
            'orderId': fake.uuid4(),
            'userId': fake.uuid4(),
            'productId': fake.uuid4(),
            'quantity': randint(1, 10),
            'totalPrice': randint(100, 1000),
            'orderDate': fake.date_time_this_year(),
            'shippingAddress': fake.address(),
            'paymentMethod': fake.credit_card_provider(),
        })

    @task(3)
    def get_product(self) -> None:
        self.client.get("api/Product")
    
    @task(4)
    def post_product(self) -> None:
        self.client.post("api/Product", json={
            'productId': fake.uuid4(),
            'name': fake.word(),
            'category': fake.word(),
        })

    @task(5)
    def get_user(self) -> None:
        self.client.get("api/User")

    @task(6)
    def post_user(self) -> None:
        self.client.post("api/User", json={
            'userId': fake.uuid4(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'dateOfBirth': fake.date_of_birth(),
        })