from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    postal_code: int

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # Rebuild the model to handle forward references

address = Address(
    street="123 Main St", 
    city="Anytown", 
    postal_code=12345
)

user = User(
    id=1,
    name="Chai Shai",
    address=address
)

comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(
            id=2,
            content="Reply1"
        ),
        Comment(
            id=3,
            content="Reply2"
        )
    ]
)