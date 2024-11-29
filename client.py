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

        if response.status_code == 201:
        print(f"Product added successfully: {response.json()}")
    else:
        print(f"Error adding product: {response.text}")

def get_products():
    response = requests.get(f'{BASE_URL}/products')
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(json.dumps(product, indent=2))
    else:
        print(f"Error retrieving products: {response.text}")

if __name__ == '__main__':
    # Add a few products
    add_product('Laptop', 'High-performance laptop', 999.99)
    add_product('Smartphone', 'Latest smartphone model', 599.99)

    # Get all products
    print("\nAll Products:")
    get_products()