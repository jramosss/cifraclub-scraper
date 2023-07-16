import pytest
from src.scraper import get_chords, get_raw

@pytest.mark.parametrize("url, expected_chords, has_solo", [
    ("https://www.cifraclub.com/cuarteto-de-nos/el-puton-del-barrio/", {"A5", "D5", "E5", "F#5", "A"}, True),
    ("https://www.cifraclub.com/fabiana-cantilo/mi-enfermedad/", {"A", "D", "E", "F#m"}, False),  # It does, but cifraclub doesn't lol
    ("https://www.cifraclub.com/marcela-morelo/luz-del-cielo/", {"C#m", "A", "B", "E", "G"}, False)
])
def test_get_chords(url, expected_chords, has_solo):
    raw = get_raw(url)
    chords, solo = get_chords(raw)
    assert chords == expected_chords
    assert solo == has_solo