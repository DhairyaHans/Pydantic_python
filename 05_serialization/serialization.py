from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
        }
    )

# Create a user instance
user = User(
    id=1,
    name="Choco",
    email="choco@pie.com",
    created_at=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="123 Chocolate Lane",
        city="Sweet City",
        pincode="12345"
    ),
    tags=["premium", "subscriber"]
)


# Using model_dump() to serialize the model to a dictionary
user_dict = user.model_dump()
print(user_dict)

print('-' * 20)

# Using model_dump_json() to serialize the model to a JSON string
json_str = user.model_dump_json()
print(json_str)