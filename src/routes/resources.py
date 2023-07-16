from fastapi import APIRouter
from src.scraper import get_chords, get_lyrics, get_raw

router = APIRouter()

@router.get("/chords")
def chords(url: str):
    raw = get_raw(url)
    return {"chords": get_chords(raw)}


@router.get("/raw")
def raw(url: str):
    return {"raw": get_raw(url)}


@router.get("/lyrics")
def lyrics(url: str):
    raw = get_raw(url)
    return {"lyrics": get_lyrics(raw)}