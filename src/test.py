import unittest
import json
from main import app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_user(self):
        response = self.app.post('/create_user',
                                 data=json.dumps(dict(user_id="1", first_name="John", last_name="Doe",
                                                 email="john@example.com", password="password", date_of_birth="2000-01-01")),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_product(self):
        response = self.app.post('/add_product',
                                 data=json.dumps(dict(
                                     product_id="1", name="Product 1", category="Category 1", price=100.0, stock=10)),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_order(self):
        response = self.app.put('/update_order/1',
                                data=json.dumps(dict(quantity=1, total_price=100.0, order_date="2022-01-01",
                                                shipping_address="Address 1", payment_method="Credit Card", payment_status="Paid")),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
