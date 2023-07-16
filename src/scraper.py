import requests
from bs4 import BeautifulSoup
from src.utils import is_chord


def get_raw(url: str):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    pre_section = soup.find("pre")

    output = pre_section.get_text().splitlines()
    splitted = [x.split(' ') for x in output]
    return list(filter(lambda x: x != '', splitted))

def get_chords(raw: list[str]):
    chords = []
    has_solo = False

    for line in raw:
        if '-' in line[0]:
            has_solo = True
        elif any(is_chord(x) for x in line):
            chords.extend([x for x in line if is_chord(x)])

    return set(chords), has_solo

def get_lyrics(raw: list[str]):
    lyrics = []

    for line in raw:
        if not any(is_chord(x) for x in line):
            lyrics.extend(line)
            lyrics.append('\n')

    return ' '.join(lyrics)

