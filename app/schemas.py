from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

class StudentMarks(BaseModel):
    school_id: int = None
    year_id: int = None
    student_id: int = None
    marks:int = None
    grade: str = ""
    subject_id: int = None
    exam_id: int = None
    IsDelete: int = 0
    