from datetime import date

from app.schemas.day import DaySummary
from app.repositories.scan_repository import ScanRepository


class DayService: 
    DAILY_LIMIT = 2000 # macro for daily limit

    def __init__(self, repository: ScanRepository): # constructor method
        self.repository = repository    # when you create a construtor, when you create an object from this class, this method will auto run


    def get_summary(self, target_date: date) -> dict:
        eaten = self.repository.summary_by_date(target_date)

        remaining = self.DAILY_LIMIT - eaten
        status = "green" if eaten <= self.DAILY_LIMIT else "red"

        return DaySummary(
            date=target_date,
            limit=self.DAILY_LIMIT,
            eaten=eaten,
            remaining=remaining,
            status=status,
        )