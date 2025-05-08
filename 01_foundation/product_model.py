from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

input_json = {
    "id": 404,
    "name": "laptop",
    "price": 9999.99,
}

prod = Product(**input_json)
print(prod)