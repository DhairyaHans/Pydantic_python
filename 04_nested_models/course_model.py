"""
    TODO: Create a course model such that
        - Each course has modules
        - Each module has lessons
"""

from pydantic import BaseModel
from typing import List


class Lesson(BaseModel):
    id: int
    title: str
    description: str

class Module(BaseModel):
    id: int
    moduele_name: str
    lessons: List[Lesson]

class Course(BaseModel):
    id: int
    course_name: str
    modules: List[Module]
    price: float
