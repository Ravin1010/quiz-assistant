from pathlib import Path

from .engine import BaseOCREngine
from .models import OCRResult


class EasyOCREngine(BaseOCREngine):

    def __init__(self):
        import easyocr

        self.reader = easyocr.Reader(["en"])

    def read(self, image_path: str | Path) -> list[OCRResult]:
        raw = self.reader.readtext(str(image_path))

        results = []

        for _, text, confidence in raw:
            results.append(
                OCRResult(
                    text=text,
                    confidence=float(confidence),
                )
            )

        return results