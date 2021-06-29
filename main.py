import csv
from lxml import etree

def _bold(str):
    return f"**{str}**"

def _spoiler(str):
    return f"||{str}||"

def open_tsv():
    custom_dict = {}
    with open("./data/ja_pitch_accents.tsv") as tsv:
        reader = csv.DictReader(tsv, delimiter="\t", quotechar='"')
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
    parser = etree.XMLParser(dtd_validation=True)
    tree: etree._ElementTree = etree.parse("./data/JMdict_e_examp.xml", parser)
    path = f"//keb[text()='{word}']/ancestor::entry/sense/gloss | //reb[text()='{word}']/ancestor::entry/sense/gloss"
    print(path)
    element: list[etree._Element] = tree.xpath(path)

    return [gloss.text for gloss in element]

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
        _spoiler(f'{", ".join(definitions)}')
    )

if __name__ == "__main__":
    main()
