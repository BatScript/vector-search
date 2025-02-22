from fastapi import APIRouter, HTTPException
from db.mongo import Database
from src.services.vector_search import perform_vector_search

router = APIRouter()

@router.get("/search")
async def search(query: str):
    try:
        # Get the database client
        db = Database.get_database("product_search")
        
        # Call the vector search function
        data = await perform_vector_search(db, query)

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

