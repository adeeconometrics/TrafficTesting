from typing import Deque, Final
from random import randint, choice
from collections import deque

from faker import Faker
from locust import HttpUser, task, between

fake = Faker()

class UserBehaviorAsp(HttpUser):
    _maxlen: Final[int] = 5
    _product_id: str = ''
    _user_id: str = ''
    _order_id: str = ''
    
    wait_time = between(1, 2.5)
    
    product_ids: Deque[str] = deque(maxlen=_maxlen)
    user_ids: Deque[str] = deque(maxlen=_maxlen)
    order_ids: Deque[str] = deque(maxlen=_maxlen)

    @task(1)
    def post_product(self) -> None:
        self._product_id = fake.uuid4()
        if len(self.product_ids) == self._maxlen:
            self.product_ids.append(self._product_id)

        self.client.post("api/Product", json={
            'productId': self._product_id,
            'name': fake.word(),
            'category': fake.word(),
        })

    @task(2)
    def get_product(self) -> None:
        self.client.get("api/Product")

    @task(3)
    def get_product_id(self) -> None:
        if self.product_ids:
            self.client.get(f"api/Product/{choice(self.product_ids)}")
    
    @task(4)
    def put_product_id(self) -> None:
        if self.product_ids:
            chosen_product_id:str = choice(self.product_ids)
            self.client.put(f"api/Product/{chosen_product_id}", json={
                'productId': chosen_product_id,
                'name': fake.name(),
                'category': fake.word(),
            })

    @task(4)
    def post_user(self) -> None:
        self.client.post("api/User", json={
            'userId': fake.uuid4(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'dateOfBirth': str(fake.date_of_birth()),
        })

    @task(5)
    def get_user(self) -> None:
        self.client.get("api/User")

    @task(6)
    def get_order(self) -> None:
        self.client.get("api/Order")

    @task(7)
    def post_order(self) -> None:
        self.client.post("api/Order", json={
            'orderId': fake.uuid4(),
            'userId': fake.uuid4(),
            'productId': fake.uuid4(),
            'quantity': randint(1, 10),
            'totalPrice': randint(100, 1000),
            'orderDate': str(fake.date_time_this_year()),
            'shippingAddress': fake.address(),
            'paymentMethod': fake.credit_card_provider(),
        })
