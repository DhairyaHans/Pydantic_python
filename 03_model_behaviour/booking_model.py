"""
    TODO: Create a Booking Model, with the following fields:
        - user_id: int
        - room_id: int
        - nights: int (must be >= 1)
        - rate_per_night: float

    Also, Add computed field:
        - total_cost: nights * rate_per_night            
"""

from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night