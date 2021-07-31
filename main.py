from lxml import etree
import random
from textwrap import dedent

from data import Data
from discord_format import DiscordFormat
from sentence_pair import SentencePair

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
