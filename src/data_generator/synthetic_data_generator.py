import random
from typing import List, Dict
from faker import Faker

fake = Faker()

def generate_synthetic_products(num_records: int = 100) -> List[Dict]:
    """
    Generate synthetic product data for testing vector search capabilities.
    The data includes various fields that could be used for vector embeddings and search.
    
    Args:
        num_records: Number of synthetic records to generate
        
    Returns:
        List of dictionaries containing product data
    """
    products = []
    
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports', 
                 'Beauty', 'Toys', 'Food & Beverage', 'Automotive', 'Health']
    
    brands = ['TechPro', 'StyleCo', 'HomeLife', 'BookWorld', 'SportMaster',
              'BeautyPlus', 'ToyJoy', 'FoodFest', 'AutoMax', 'HealthFirst']
    
    for _ in range(num_records):
        product = {
            'id': fake.uuid4(),
            'name': fake.catch_phrase(),
            'description': fake.text(max_nb_chars=200),
            'category': random.choice(categories),
            'subcategory': fake.word(),
            'brand': random.choice(brands),
            'price': round(random.uniform(10, 1000), 2),
            'rating': round(random.uniform(1, 5), 1),
            'num_reviews': random.randint(0, 1000),
            'features': [fake.word() for _ in range(random.randint(3, 8))],
            'tags': [fake.word() for _ in range(random.randint(2, 6))],
            'color': fake.color_name(),
            'material': fake.word(),
            'dimensions': {
                'length': round(random.uniform(1, 100), 2),
                'width': round(random.uniform(1, 100), 2),
                'height': round(random.uniform(1, 100), 2),
            },
            'weight': round(random.uniform(0.1, 50), 2),
            'manufacturer_location': fake.country(),
            'in_stock': random.choice([True, False]),
            'stock_quantity': random.randint(0, 1000),
            'release_date': str(fake.date_between(start_date='-5y', end_date='today')),
            'warranty_months': random.choice([0, 12, 24, 36, 48, 60]),
            'metadata': {
                'sustainable': random.choice([True, False]),
                'recyclable': random.choice([True, False]),
                'organic': random.choice([True, False]),
                'hand,made': random.choice([True, False])
            }
        }
        products.append(product)
    
    return products

if __name__ == "__main__":
    # Generate sample data
    sample_data = generate_synthetic_products(10)
    # Print first record as example
    print(sample_data[0])
