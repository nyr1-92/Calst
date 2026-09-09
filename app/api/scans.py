from fastapi import APIRouter, HTTPException

from app.database import SessionLocal
from app.repositories.scan_repository import ScanRepository
from app.schemas.scan import Scan, ScanCreate
from app.services.scan_service import ScanService

router = APIRouter()

# a new beginning

@router.get("/scans", response_model=list[Scan])
def get_scans():
    with SessionLocal() as session:  # Create a database session when this API called
        repository = ScanRepository(session)    # inform repository we are going to use this session for db connection
        service = ScanService(repository) # use the service to get scans but get it from the database. 
        return service.get_scans()

@router.post("/scans", response_model=Scan)
def create_scan(scan: ScanCreate):
    with SessionLocal() as session:
        repository = ScanRepository(session)
        service = ScanService(repository)
        return service.create_scan(scan)

@router.get("/scans/{scan_id}", response_model=Scan)
def get_scan(scan_id: int):
    with SessionLocal() as session:
        repository = ScanRepository(session)
        service = ScanService(repository)

        scan = service.get_scan(scan_id)

        if scan is None:
            raise HTTPException(
                status_code=404,
                detail="Scan not found",
            )

        return scan

@router.delete("/scans/{scan_id}", response_model=Scan)
def delete_scan(scan_id: int):
    with SessionLocal() as session:
        repository = ScanRepository(session)
        service = ScanService(repository)

        deleted = service.delete_scan(scan_id)

        if deleted is False:
            raise HTTPException(
                status_code=404,
                detail="Scan not found",
            )

        return True