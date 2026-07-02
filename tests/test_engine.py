from app.ocr import EasyOCREngine


def test_engine_initialization():
    engine = EasyOCREngine()
    assert engine is not None