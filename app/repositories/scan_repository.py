from sqlalchemy import select, DateTime, func
from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta

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

    def delete(self, scan_id: int) -> bool:
        scan = self.session.get(ScanModel, scan_id)

        if scan is None:
            return False

        self.session.delete(scan)
        self.session.commit()

        return True

    def summary_by_date(self, target_date: date) -> int:
        # This can be a great layout for database queries
        # we are not writing raw SQL so we are determining the query and calling the methods to handle it.

        start = datetime.combine(target_date, datetime.min.time())
        end = start + timedelta(days=1)

        statement = select(
            func.coalesce(func.sum(ScanModel.estimated_calories), 0)
        ).where(
            ScanModel.created_at >= start,
            ScanModel.created_at < end,
        )

        return self.session.scalar(statement)

    def history(self):
        statement = (
            select(
                func.date(ScanModel.created_at).label("date"),
                func.sum(ScanModel.estimated_calories).label("eaten"),
            )
            .group_by(func.date(ScanModel.created_at))
            .order_by(func.date(ScanModel.created_at).desc())
        )

        return self.session.execute(statement).all()