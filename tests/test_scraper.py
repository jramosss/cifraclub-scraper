import pytest
from src.scraper import get_chords, get_raw

@pytest.mark.parametrize("url, expected", [
    ("https://www.cifraclub.com/fabiana-cantilo/mi-enfermedad/", {"A", "D", "E", "F#m"}),
    # ("https://www.cifraclub.com/marcela-morelo/luz-del-cielo/", {"C#m", "A", "B", "E"})
])
def test_get_chords(url, expected):
    raw = get_raw(url)
    assert get_chords(raw) == expected