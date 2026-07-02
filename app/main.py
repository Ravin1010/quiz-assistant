from pathlib import Path

from app.ocr import EasyOCREngine


def main():
    engine = EasyOCREngine()

    results = engine.read(
        Path("screenshots/mcq1.png")
    )

    for result in results:
        print(result)


if __name__ == "__main__":
    main()