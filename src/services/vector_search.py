from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def cosine_similarity(query_embedding, query_norm, product_embedding):
    product_norm = np.linalg.norm(product_embedding)
    return np.dot(query_embedding, product_embedding) / (query_norm * product_norm)

async def perform_vector_search(db, query: str):
    # Fetch all products from the database
    results = await db["products"].find({}, {"_id": 0}).to_list(length=None)
    
    # Encode the query and compute its norm once
    query_embedding = model.encode(query)
    query_norm = np.linalg.norm(query_embedding)

    product_similarities = []

    # Iterate over each product to compute similarity
    for product in results:
        # Convert embeddings to numpy arrays if they aren't already
        name_embedding = np.array(product["embedding"]["name"])
        desc_embedding = np.array(product["embedding"]["description"])
        
        # Compute cosine similarities for both name and description
        name_sim = cosine_similarity(query_embedding, query_norm, name_embedding)
        desc_sim = cosine_similarity(query_embedding, query_norm, desc_embedding)
        
        sim = max(name_sim, desc_sim)
        
        # Apply threshold filtering
        if sim > 0.3:
            product_similarities.append((product, sim))

    # Sort products by similarity score in descending order and select the top 5
    product_similarities.sort(key=lambda x: x[1], reverse=True)
    top_5_products = product_similarities[:5]

    data = []
    for product, sim in top_5_products:
        # Remove embedding information and attach the computed similarity score
        product_without_embedding = {k: v for k, v in product.items() if k != 'embedding'}
        product_without_embedding['similarity_score'] = sim
        data.append(product_without_embedding)

    return data
