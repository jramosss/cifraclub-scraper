import pytest
from src.utils import is_chord

@pytest.mark.parametrize("chord, expected", [
    ("C", True),
    ("C#", True),
    ("Cm", True),
    ("C#m", True),
    ("C7", True),
    ("C#7", True),
    ("Cm7", True),
    ("C#m7", True),
    ("H", False),
    ("H#", False),
    ("X", False),
    ("(", False)
])
def test_is_chord(chord, expected):
    assert is_chord(chord) == expected