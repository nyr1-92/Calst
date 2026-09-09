from typing import Optional
import logging

from app.repositories.scan_repository import ScanRepository
from app.schemas.scan import Scan, ScanCreate

logger = logging.getLogger(__name__)


class ScanService:
    def __init__(self, repository: ScanRepository): # dependency injection for modular programming
        self.repository = repository

    def get_scans(self) -> list[Scan]:
        return self.repository.get_all()

    def create_scan(self, scan: ScanCreate) -> Scan:
        logger.info("Create data point")

        try:
            created_entry = self.repository.create(scan)
            logger.info("Entry with %s created successfully.", created_entry.id)
            return created_entry
        except Exception:
            logger.exception("Failed to create scan, reason: %s", Exception)
            raise


    def get_scan(self, scan_id: int) -> Optional[Scan]:
        logger.info("Fetching scan with id=%s", scan_id)
        scan = self.repository.get_by_id(scan_id)

        if scan is None:
            logger.warning("Scan not found id=%s", scan_id)

        return scan

    def delete_scan(self, scan_id: int) -> Optional[bool]:
        logger.info("Deleting the entry with ID: %s", scan_id)
        deleted_entry = self.repository.delete(scan_id)
        if deleted_entry:
            logger.info("Entry ID: %s deleted successfully", scan_id)
            return True
        else:
            logger.error("Failed to delete")
            return False
