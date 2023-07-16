import requests
from bs4 import BeautifulSoup
from src.utils import is_chord


def get_raw(url: str):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    pre_section = soup.find("pre")

    return pre_section.get_text().splitlines()

def get_chords(raw: list[str]):
    chords = []
    has_solo = False

    for line in raw:
        if not line.strip():
            continue
        
        splitted_line = list(filter(lambda x: x != '', line.split(' ')))
        if '-' in splitted_line[0]:
            has_solo = True
        elif any(is_chord(x) for x in splitted_line):
            chords.extend([x for x in splitted_line if is_chord(x)])

    return set(chords), has_solo

def get_lyrics(raw: list[str]):
    lyrics = []

    for line in raw:
        if not line.strip():
            continue
        
        splitted_line = list(filter(lambda x: x != '', line.split(' ')))
        if not any(is_chord(x) for x in splitted_line):
            lyrics.extend(splitted_line)
            lyrics.append('\n')

    return ' '.join(lyrics)

