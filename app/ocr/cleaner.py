import re


class TextCleaner:
    """Normalizes OCR output into predictable text."""

    def normalize_quotes(self, text: str) -> str:
        replacements = {
            "“": '"',
            "”": '"',
            "‘": "'",
            "’": "'",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def normalize_dashes(self, text: str) -> str:
        return (
            text.replace("–", "-")
                .replace("—", "-")
        )

    def remove_extra_whitespace(self, text: str) -> str:
        text = re.sub(r"[ \t]+", " ", text)
        return text.strip()

    def remove_empty_lines(self, text: str) -> str:
        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        return "\n".join(lines)

    def __init__(self):
        self.pipeline = [
            self.normalize_quotes,
            self.normalize_dashes,
            self.remove_extra_whitespace,
            self.remove_empty_lines,
        ]

    def clean(self, text):
        for step in self.pipeline:
            text = step(text)
        return text