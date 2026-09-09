from app.repositories.scan_repository import ScanRepository
from app.schemas.history import HistoryEntry


class HistoryService:
    DAILY_LIMIT = 2000

    def __init__(self, repository: ScanRepository):
        self.repository = repository

    def get_history(self) -> list[HistoryEntry]:
        rows = self.repository.history()

        history = []

        for row in rows:
            eaten = row.eaten
            remaining = self.DAILY_LIMIT - eaten
            status = "green" if eaten <= self.DAILY_LIMIT else "red"

            history.append(
                HistoryEntry(
                    date=row.date,
                    eaten=eaten,
                    limit=self.DAILY_LIMIT,
                    remaining=remaining,
                    status=status,
                )
            )

        return history