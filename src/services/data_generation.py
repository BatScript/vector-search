from sentence_transformers import SentenceTransformer
from src.data_generator.synthetic_data_generator import generate_synthetic_products
from db.mongo import Database

async def generate_synthetic_data():
    products = generate_synthetic_products(100)
    db = Database.get_database("product_search")
    result = await db["products"].insert_many(products)
    return len(result.inserted_ids)

async def generate_product_embeddings():
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    db = Database.get_database("product_search")
    products = await db["products"].find().to_list(None)
    embeddings_count = 0

    for product in products:
        embeddings = {
            'name': model.encode(product['name']).tolist(),
            'description': model.encode(product['description']).tolist()
        }
        await db["products"].update_one(
            {"_id": product["_id"]},
            {"$set": {"embedding": embeddings}}
        )
        embeddings_count += 1

    return embeddings_count 