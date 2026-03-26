from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session


DATABASE_URL = "mysql+pymysql://SaiSai:saisai123@34.45.235.19:3306/free-trial-first-project"



# Setup DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

app = FastAPI(title="Hotels API")


# DATABASE MODEL
class Hotel(Base):
    __tablename__ = "hotels"   

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)


# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Schemas
class HotelCreate(BaseModel):
    name: str
    neighborhood: str
    price_per_night: float


class HotelResponse(HotelCreate):
    id: int

    class Config:
        from_attributes = True   


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# ROUTES

# 1. CREATE
@app.post("/hotels", response_model=HotelResponse)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel


# 2. GET BY ID
@app.get("/hotels/{hotel_id}", response_model=HotelResponse)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel


# 3. LIST ALL
@app.get("/hotels", response_model=list[HotelResponse])
def list_hotels(db: Session = Depends(get_db)):
    return db.query(Hotel).all()