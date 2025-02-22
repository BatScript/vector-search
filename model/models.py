from pydantic import BaseModel

class GenerateDataResponse(BaseModel):
    message: str
    products_inserted: int

class GenerateEmbeddingsResponse(BaseModel):
    message: str
    embeddings_generated: int 