from pydantic import BaseModel

class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    description: str

    class Config:
        from_attributes = True