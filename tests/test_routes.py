import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


@pytest.mark.parametrize("url, expected_chords, has_solo", [
    ("https://www.cifraclub.com/cuarteto-de-nos/el-puton-del-barrio/", set(["A5", "D5", "E5", "F#5", "A"]), True),
])
def test_get_chords(url, expected_chords, has_solo):
    response = client.get(f"/chords?url={url}")
    assert response.status_code == 200
    assert response.json() == {"chords": expected_chords, "has_solo": has_solo}
