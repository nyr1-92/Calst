from typing import Optional

from app.repositories.scan_repository import ScanRepository
from app.schemas.scan import Scan, ScanCreate


class ScanService:
    def __init__(self, repository: ScanRepository): # dependency injection for modular programming
        self.repository = repository

    def get_scans(self) -> list[Scan]:
        return self.repository.get_all()

    def create_scan(self, scan: ScanCreate) -> Scan:
        return self.repository.create(scan)

    def get_scan(self, scan_id: int) -> Optional[Scan]:
        return self.repository.get_by_id(scan_id)


