from pathlib import Path

from .models import OCRResult


class OCREngine:
    def __init__(self):
        import easyocr

        self.reader = easyocr.Reader(["en"])

    def read(self, image_path: str | Path) -> list[OCRResult]:
        raise NotImplementedError