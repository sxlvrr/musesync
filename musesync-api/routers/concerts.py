from fastapi import APIRouter
from sqlalchemy import text
from database import SessionLocal

router = APIRouter()

@router.get("/")
def get_concerts():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM concerts;"))
    concerts = [dict(row._mapping) for row in result]
    db.close()
    return concerts
