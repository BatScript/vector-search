from fastapi import APIRouter, HTTPException
from model.models import GenerateDataResponse, GenerateEmbeddingsResponse
from src.services.data_generation import generate_synthetic_data, generate_product_embeddings

router = APIRouter()

@router.get("/generate-data", response_model=GenerateDataResponse)
async def generate_data():
    try:
        products_inserted = await generate_synthetic_data()
        return GenerateDataResponse(
            message="Successfully generated and stored synthetic data",
            products_inserted=products_inserted
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@router.get("/generate-embeddings", response_model=GenerateEmbeddingsResponse)
async def generate_embeddings():
    try:
        embeddings_generated = await generate_product_embeddings()
        return GenerateEmbeddingsResponse(
            message="Successfully generated and stored embeddings",
            embeddings_generated=embeddings_generated
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
