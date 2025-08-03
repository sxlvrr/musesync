from fastapi import APIRouter
from sqlalchemy import text
from database import SessionLocal

router = APIRouter()

@router.get("/")
def get_ecoutes():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM ecoutes;"))
    ecoutes = [dict(row._mapping) for row in result]
    db.close()
    return ecoutes
