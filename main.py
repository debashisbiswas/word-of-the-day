import csv
from lxml import etree

class Data:
    def __init__(self, *, jisho_path, tsuneyo_path):
        self.jisho = self._init_jisho(jisho_path)
        self.tsuneyo = self._init_tsuneyo(tsuneyo_path)

    def _init_jisho(self, path: str):
        parser = etree.XMLParser(dtd_validation=True)
        return etree.parse(path, parser)

    def _init_tsuneyo(self, path: str):
        custom_dict = {}
        with open(path) as tsv:
            reader = csv.DictReader(tsv, delimiter="\t", quotechar='"')
            for row in reader:
                custom_dict[row['word']] = {
                    "kana": row['kana'],
                    "accent": row['accent']
                }
        return custom_dict

    def get_jisho(self):
        return self.jisho

    def get_tsuneyo(self):
        return self.tsuneyo

def _bold(str):
    return f"**{str}**"

def _spoiler(str):
    return f"||{str}||"

def get_reading(word: str, *, data: Data) -> str:
    custom_dict = data.get_tsuneyo()

    return custom_dict[word]['kana'] if word in custom_dict else ''

def get_accent(word: str, *, data: Data) -> int:
    custom_dict = data.get_tsuneyo()

    return custom_dict[word]['accent'] if word in custom_dict else 0

def get_definitions(word: str, *, data: Data) -> str:
    jisho = data.get_jisho()
    path = f"//keb[text()='{word}']/ancestor::entry/sense/gloss | //reb[text()='{word}']/ancestor::entry/sense/gloss"
    element: list[etree._Element] = jisho.xpath(path)

    return [gloss.text for gloss in element]

def main():
    print("Setting up...")
    sources = Data(
        jisho_path="./data/JMdict_e_examp.xml",
        tsuneyo_path="./data/ja_pitch_accents.tsv"
    )

    selected_word = input("Which word would you like to use? > ")
    reading = get_reading(selected_word, data=sources)
    pitch = get_accent(selected_word, data=sources)
    definitions = get_definitions(selected_word, data=sources)

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
