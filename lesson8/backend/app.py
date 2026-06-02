import os
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://crm:secret@db:5432/crmdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Deal(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(100), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), default="new")


Base.metadata.create_all(bind=engine)
app = FastAPI(title="CRM Business Logic")


class DealCreate(BaseModel):
    client_name: str
    amount: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/deals")
def list_deals(db: Session = Depends(get_db)):
    return db.query(Deal).all()


@app.post("/api/deals")
def create_deal(deal: DealCreate, db: Session = Depends(get_db)):
    db_deal = Deal(client_name=deal.client_name, amount=deal.amount)
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal
