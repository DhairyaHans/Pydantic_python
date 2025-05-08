from pydantic import BaseModel, Field
from typing import Optional

"""
    TODO: Crate a Pydantic model for an employee with the following fields:
    - id: int
    - name: str (min 3 chars)
    - department: optional str (default: 'General')
    - salary: float (must be >= 100000)
"""

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,    # ... means required field
        min_length=3,
        max_length=50,
        description="Name of the employee",
        example="Chai Shai"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        gt=100000,
        description="Salary of the employee",
        example=150000.0
    )