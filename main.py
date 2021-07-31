import csv
from lxml import etree
import random
from textwrap import dedent

from discord_format import DiscordFormat

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

class SentencePair:
    def __init__(self, jpn_sentence, eng_sentence):
        self.jpn = jpn_sentence
        self.eng = eng_sentence

def get_reading(word: str, *, data: Data) -> str:
    custom_dict = data.tsuneyo
    return custom_dict[word]['kana'] if word in custom_dict else ''

def get_accent(word: str, *, data: Data) -> int:
    custom_dict = data.tsuneyo
    return custom_dict[word]['accent'] if word in custom_dict else 0

def get_definitions(word: str, *, data: Data) -> str:
    jisho = data.jisho
    path = f"//keb[text()='{word}']/ancestor::entry/sense/gloss | //reb[text()='{word}']/ancestor::entry/sense/gloss"
    element: list[etree._Element] = jisho.xpath(path)

    return [gloss.text for gloss in element]

def get_sentences(word: str, *, data: Data) -> list[SentencePair]:
    jisho = data.jisho
    path = f"//keb[text()='{word}']/ancestor::entry/sense/example | //reb[text()='{word}']/ancestor::entry/sense/example"
    examples: list[etree._Element] = jisho.xpath(path)
    sentences: list[SentencePair] = []
    for example in examples:
        jpn = example.xpath("ex_sent[@xml:lang='jpn']")[0].text
        eng = example.xpath("ex_sent[@xml:lang='eng']")[0].text
        sentences.append(SentencePair(jpn, eng))
    return sentences

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
    sentences = get_sentences(selected_word, data=sources)
    sentence = random.choice(sentences)

    wide_space = "　"
    separator = "-" * 50
    print(dedent(f"""
        {separator}
        {DiscordFormat.bold("今日の言葉")}

        {DiscordFormat.bold(selected_word)}　{DiscordFormat.spoiler(f'{reading}　[{pitch}]')}　{DiscordFormat.spoiler(f'{", ".join(definitions)}')}

        {sentence.jpn}
        {DiscordFormat.spoiler(sentence.eng)}
        {separator}
    """))

if __name__ == "__main__":
    main()
