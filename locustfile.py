from faker import Faker
from locust import HttpUser, task, between
from random import randint

fake = Faker()

class UserBehaviorAsp(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def post_item(self):
        self.client.post("/api/TodoItems", json={
            "id": randint(1_000, 1_000_000),
            "name": fake.name(),
            "isComplete": True
        })