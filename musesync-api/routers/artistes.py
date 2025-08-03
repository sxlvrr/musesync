from fastapi import APIRouter
from sqlalchemy import text
from database import SessionLocal

router = APIRouter()

@router.get("/")
def get_artistes():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM artistes ORDER BY popularite DESC;"))
    artistes = [dict(row._mapping) for row in result]
    db.close()
    return artistes
