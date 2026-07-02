from abc import ABC, abstractmethod
from pathlib import Path

from .models import OCRResult


class BaseOCREngine(ABC):
    @abstractmethod
    def read(self, image_path: str | Path) -> list[OCRResult]:
        """Read text from an image."""
        pass