from db.mongo import Database
from fastapi import HTTPException

async def get_synthetic_data():
    try:
        # Use async methods to interact with the database
        products = await Database.get_database("product_search")['products'].find().to_list(None)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

