from typing import List

class Meta:
    status: str

class Japanese:
    word: str
    reading: str

class Sense:
    english_definitions: List[str]
    parts_of_speech: List[str]
    links: List[str]
    tags: List[str]
    restrictions: List[str]
    see_also: List[str]
    antonyms: List[str]
    source: List[str]
    info: List[str]

class Data:
    slug: str
    is_common: bool
    tags: List[str]
    jlpt: List[str]
    japanese: List[Japanese]
    senses: List[Sense]

class JishoResponse:
    meta: Meta
    data: List[Data]
