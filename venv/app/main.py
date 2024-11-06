from fastapi import FastAPI, Response, status, HTTPException, APIRouter, Depends
from fastapi.params import Body
from pydantic import BaseModel
import mysql.connector
from datetime import datetime
import app.models as models
from app.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from sqlalchemy import update,delete
import app.schemas as schemas
from app.routers import student_mark
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bh@f1mercedes",
  database="school_management"
)

mycursor = mydb.cursor(dictionary=True)
models.Base.metadata.create_all(bind=engine)

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

# origins = [
#     "https://www.google.com/"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(student_mark.router)

@app.get("/")
def root():
    return {"message": "Hi"}




#
# class StudentMarks(BaseModel):
#     school_id: int = None
#     year_id: int = None
#     student_id: int = None
#     marks:int = None
#     grade: str = ""
#     subject_id: int = None
#     exam_id: int = None
#     IsDelete: int = 0


# @app.get("/sqlalchemy")
# def test_post(db: Session = Depends(get_db)):
#     posts = db.query(models.student_marks).all()
#     return {"data": posts}

# @app.post("/sqlalchemy/marks")
# def create_post(grades: schemas.StudentMarks, db: Session = Depends(get_db)):
#     new_mark = models.student_marks(**grades.model_dump())
#     db.add(new_mark)
#     db.commit()
#     db.refresh(new_mark)
#     return{"data": new_mark}
# 
#     pass

# @app.get("/sqlalchemy/marks/{id}")
# def get_marks_id(id: int, db: Session = Depends(get_db)):
#     id_marks = db.query(models.student_marks).filter(models.student_marks.marks_id == id).first()
#     return id_marks
#     pass

# @app.delete("/sqlalchemy/marks/{id}")
# def delete_marks(id:int, db: Session = Depends(get_db)):
#     delete_post = db.query(models.student_marks).filter(models.student_marks.marks_id == id)
#     delete_post.delete(synchronize_session=False)
#     db.commit()
#     pass
# 
# 
# @app.put("/sqlalchemy/marks/{id}")
# def update_marks_id(id: int, grades: schemas.StudentMarks, db: Session = Depends(get_db)):
#     mark_change = db.query(models.student_marks).filter(models.student_marks.marks_id == id)
#     mark_change.update(grades.model_dump(), synchronize_session=False)
#     db.commit()
#     pass


@app.get("/marks")
def get_marks():
    sql_products = mycursor.execute("SELECT * FROM school_management.student_marks;")
    sql_products = mycursor.fetchall()
    return {"data": sql_products}



@app.post("/marks")
def create_post(grades: schemas.StudentMarks):
    mycursor.execute("""INSERT INTO school_management.student_marks (school_id, year_id, student_id, marks, grade, subject_id, exam_id) """
                         """VALUES (%s, %s, %s, %s, %s, %s, %s)""", (grades.school_id, grades.year_id, grades.student_id, grades.marks, grades.grade, grades.subject_id, grades.exam_id))
    new_post = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return {"message": new_post}


@app.get("/marks/{id}")
def get_marks_id(id: int):
    mycursor.execute(
        """SELECT * FROM school_management.student_marks WHERE marks_id = %s """, [(id)])
    test_marks = mycursor.fetchone()
    return {"data": test_marks}
    pass


@app.delete("/marks/{id}")
def delete_marks(id:int):
    mycursor.execute(
        """DELETE FROM school_management.student_marks WHERE marks_id = %s""", [(id)])
    deleted_post = mycursor.fetchone()
    mydb.commit()
    mydb.close()
    pass


@app.put("/marks/{id}")
def update_marks_id(id: int, grades: schemas.StudentMarks):
    mycursor.execute(
        """UPDATE school_management.student_marks SET school_id = %s, year_id = %s, student_id = %s, marks = %s, grade = %s, subject_id = %s, exam_id = %s WHERE marks_id = %s """, (
        grades.school_id, grades.year_id, grades.student_id, grades.marks, grades.grade, grades.subject_id,
        grades.exam_id, str(id)))

    updated_marks = mycursor.fetchone()
    mydb.commit()
    mydb.close()
    return {"data": updated_marks}
    pass


