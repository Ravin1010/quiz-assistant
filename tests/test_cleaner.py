from app.ocr.cleaner import TextCleaner


cleaner = TextCleaner()


def test_normalize_quotes():
    text = '“Hello”'
    assert cleaner.normalize_quotes(text) == '"Hello"'


def test_normalize_dashes():
    text = "A – B — C"
    assert cleaner.normalize_dashes(text) == "A - B - C"


def test_remove_extra_whitespace():
    text = "Hello     World"
    assert cleaner.remove_extra_whitespace(text) == "Hello World"


def test_remove_empty_lines():
    text = "A\n\n\nB\n\nC"
    assert cleaner.remove_empty_lines(text) == "A\nB\nC"


def test_clean_pipeline():
    text = """

“What   is   Python?”

A. Snake

B. Programming    language

"""

    expected = '"What is Python?"\nA. Snake\nB. Programming language'

    assert cleaner.clean(text) == expected