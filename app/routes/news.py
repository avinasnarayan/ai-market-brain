from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.news import News

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/news")
def get_news(db: Session = Depends(get_db)):
    return db.query(News).order_by(News.published_at.desc()).limit(50).all()
