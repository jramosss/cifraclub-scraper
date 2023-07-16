from fastapi import APIRouter
from src.scraper import get_chords, get_lyrics, get_raw

router = APIRouter()

@router.get("/chords")
def chords(url: str):
    raw = get_raw(url)
    chords, has_solo = get_chords(raw)
    return {"chords": chords, "has_solo": has_solo}


@router.get("/raw")
def raw(url: str):
    return {"raw": get_raw(url)}


@router.get("/lyrics")
def lyrics(url: str):
    raw = get_raw(url)
    return {"lyrics": get_lyrics(raw)}