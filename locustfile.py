from typing import Deque, Final
from random import randint, choice
from collections import deque

from faker import Faker
from locust import SequentialTaskSet, task, between, HttpUser

fake = Faker()

class TaskSequenceAsp(SequentialTaskSet):
    _maxlen: Final[int] = 5
    _product_id: str = ''
    _user_id: str = ''
    _order_id: str = ''
    
    product_ids: Deque[str] = deque(maxlen=_maxlen)
    user_ids: Deque[str] = deque(maxlen=_maxlen)
    order_ids: Deque[str] = deque(maxlen=_maxlen)

    @task
    def post_product(self) -> None:
        self._product_id = fake.uuid4()
        if len(self.product_ids) == self._maxlen:
            self.product_ids.append(self._product_id)

        self.client.post("api/Product", json={
            'productId': self._product_id,
            'name': fake.word(),
            'category': fake.word(),
        })

    @task
    def get_product(self) -> None:
        self.client.get("api/Product")

    @task
    def get_product_id(self) -> None:
        if len(self.product_ids) != 0:
            self.client.get(f"api/Product/{choice(self.product_ids)}")
    
    @task
    def put_product_id(self) -> None:
        chosen_product_id:str = choice(self.product_ids)
        self.client.put(f"api/Product/{chosen_product_id}", json={
            'productId': chosen_product_id,
            'name': fake.name(),
            'category': fake.word(),
        })

    @task
    def post_user(self) -> None:
        self.client.post("api/User", json={
            'userId': fake.uuid4(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
            'dateOfBirth': str(fake.date_of_birth()),
        })

    @task
    def get_user(self) -> None:
        self.client.get("api/User")

    @task
    def get_user_id(self) -> None:
        if self.user_ids:
            self.client.get(f"api/User/{choice(self.user_ids)}")

    @task
    def put_user_id(self) -> None:
        if self.user_ids:
            chosen_user_id:str = choice(self.user_ids)
            self.client.put(f"api/User/{chosen_user_id}", json={
                'userId': chosen_user_id,
                'firstName': fake.first_name(),
                'lastName': fake.last_name(),
                'email': fake.email(),
                'password': fake.password(),
                'dateOfBirth': str(fake.date_of_birth()),
            })

    @task
    def get_order(self) -> None:
        self.client.get("api/Order")

    @task
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

    @task
    def get_order_id(self) -> None:
        if self.order_ids:
            self.client.get(f"api/Order/{choice(self.order_ids)}")

    @task
    def put_order_id(self) -> None:
        if self.order_ids:
            chosen_order_id:str = choice(self.order_ids)
            self.client.put(f"api/Order/{chosen_order_id}", json={
                'orderId': chosen_order_id,
                'userId': fake.uuid4(),
                'productId': fake.uuid4(),
                'quantity': randint(1, 10),
                'totalPrice': randint(100, 1000),
                'orderDate': str(fake.date_time_this_year()),
                'shippingAddress': fake.address(),
                'paymentMethod': fake.credit_card_provider(),
            })


class AspNetHttpUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [TaskSequenceAsp]