from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func

import app.models as models
import app.schemas as schemas
from app.database import get_db
router = APIRouter()

@router.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.student_marks).all()
    return {"data": posts}

@router.post("/sqlalchemy/marks")
def create_post(grades: schemas.StudentMarks, db: Session = Depends(get_db)):
    new_mark = models.student_marks(**grades.model_dump())
    db.add(new_mark)
    db.commit()
    db.refresh(new_mark)
    return{"data": new_mark}

    pass



@router.get("/sqlalchemy/marks/{id}")
def get_marks_id(id: int, db: Session = Depends(get_db)):
    id_marks = db.query(models.student_marks).filter(models.student_marks.marks_id == id).first()
    return id_marks
    pass

@router.delete("/sqlalchemy/marks/{id}")
def delete_marks(id:int, db: Session = Depends(get_db)):
    delete_post = db.query(models.student_marks).filter(models.student_marks.marks_id == id)
    delete_post.delete(synchronize_session=False)
    db.commit()
    pass


@router.put("/sqlalchemy/marks/{id}")
def update_marks_id(id: int, grades: schemas.StudentMarks, db: Session = Depends(get_db)):
    mark_change = db.query(models.student_marks).filter(models.student_marks.marks_id == id)
    mark_change.update(grades.model_dump(), synchronize_session=False)
    db.commit()
    pass