from fastapi import FastAPI
from app.api.scans import router as scans_router

from app.database import engine
from app.models.scan import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Calst API")
app.include_router(scans_router)

@app.get("/")
def root():
    return {"message": "Calst backend is running"}