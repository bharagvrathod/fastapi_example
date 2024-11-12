from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
from sqlalchemy import update, delete

class student_marks(Base):
    __tablename__ = "student_marks"

    marks_id = Column(Integer, primary_key=True, nullable=False)
    school_id = Column(Integer, nullable=True)
    year_id = Column(Integer, nullable=True)
    student_id = Column(Integer, nullable=True)
    marks = Column(Integer, nullable=True)
    grade = Column(String(10), nullable=True)
    subject_id = Column(Integer, nullable=True)
    exam_id = Column(Integer, nullable=True)

    CreateDTTM = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text('now()'))
    UpdateDTTM = Column(TIMESTAMP(timezone=True),
                        nullable=True, server_default=text('now()'))
    IsDelete = Column(Integer, default=0,nullable=False)
