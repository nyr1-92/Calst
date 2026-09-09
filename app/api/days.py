from datetime import date

from fastapi import APIRouter

from app.database import SessionLocal
from app.repositories.scan_repository import ScanRepository
from app.schemas.day import DaySummary
from app.services.day_service import DayService

router = APIRouter()


@router.get("/days/{target_date}", response_model=DaySummary)
def get_day_summary(target_date: date):
    with SessionLocal() as session:
        repository = ScanRepository(session)
        service = DayService(repository)

        return service.get_summary(target_date)