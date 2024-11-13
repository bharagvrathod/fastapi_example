from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pymysql
import pymysql.cursors
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="Bh@f1mercedes",  # plain (unescaped) text
    host="localhost",
    database="school_management",
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit = False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()