import csv
from typing import Dict
import requests

def _bold(str):
    return f"**{str}**"

def _spoiler(str):
    return f"||{str}||"

def open_tsv() -> Dict:
    custom_dict = {}
    with open("./pitch_data/ja_pitch_accents.tsv") as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t", quotechar='"')
        for row in reader:
            custom_dict[row['word']] = {
                "kana": row['kana'],
                "accent": row['accent']
            }

    return custom_dict

def get_reading(word: str) -> str:
    custom_dict = open_tsv()

    return custom_dict[word]['kana'] if word in custom_dict else ''

def get_accent(word: str) -> int:
    custom_dict = open_tsv()

    return custom_dict[word]['accent'] if word in custom_dict else 0

def get_definitions(word: str) -> str:
    r = requests.get("https://jisho.org/api/v1/search/words", { "keyword": word })
    if r.status_code != 200:
        print(f"Request to Jisho failed.")
        print(f"Status code: {r.status_code}")
        print(r.reason)
        return

    definitions = []
    for row in r.json()['data'][0]['senses']:
        definitions += row['english_definitions']

    return definitions

def main():
    selected_word = input("Which word would you like to use? > ")
    reading = get_reading(selected_word)
    pitch = get_accent(selected_word)
    definitions = get_definitions(selected_word)

    wide_space = "　"
    print(_bold("今日の言葉"))
    print()
    print(
        _bold(selected_word) +
        wide_space +
        _spoiler(f'{reading}　[{pitch}]') +
        wide_space +
        _spoiler(f'{"; ".join(definitions)}')
    )

if __name__ == "__main__":
    main()
