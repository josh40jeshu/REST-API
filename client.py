import requests
import json

BASE_URL = 'http://localhost:5000'

def add_product(name, description, price):
    payload = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(f'{BASE_URL}/products', json=payload)