from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.scan import ScanModel
from app.schemas.scan import ScanCreate

from typing import Optional

class ScanRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[ScanModel]:
        statement = select(ScanModel)
        result = self.session.scalars(statement)

        return list(result)

    def get_by_id(self, scan_id: int) -> Optional[ScanModel]:
        return self.session.get(ScanModel, scan_id)

    def create(self, scan: ScanCreate) -> ScanModel:
        db_scan = ScanModel(
            food_description=scan.food_description,
            estimated_calories=scan.estimated_calories,
            min_calories=scan.min_calories,
            max_calories=scan.max_calories,
            confidence=scan.confidence,
        )

        self.session.add(db_scan)
        self.session.commit()
        self.session.refresh(db_scan)

        return db_scan