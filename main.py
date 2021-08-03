import argparse
import random
from textwrap import dedent

from data import Data
from discord_format import DiscordFormat as df
from word import Word

WIDE_SPACE = "　"

def _get_header_string() -> str:
    return df.bold("今日の言葉")

def _get_word_string(word: Word) -> str:
    return WIDE_SPACE.join([
        df.bold(word.word),
        df.spoiler(f"{word.reading}　[{word.pitch if word.pitch != -1 else '?'}]"),
        df.spoiler(f"{', '.join(word.definitions)}")
    ])

def _get_sentence_string(word: Word) -> str:
    if word.sentences:
        sentence = random.choice(word.sentences)
        return dedent(f"""
            {sentence.jpn if sentence else ''}
            {df.spoiler(sentence.eng) if sentence else ''}
        """).strip()
    else:
        return ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs="?",
                        help="selected word for word of the day message")
    args = parser.parse_args()

    print("Setting up...")
    sources = Data(
        jisho_path="./data/JMdict_e_examp.xml",
        tsuneyo_path="./data/ja_pitch_accents.tsv"
    )

    if args.word:
        selected_word = args.word
    else:
        selected_word = input("Which word would you like to use? > ")
    print(f"Proceeding with word: {selected_word}")
    word = Word(selected_word, data=sources)

    output_components = []
    output_components.append(_get_header_string())

    if not word.definitions:
        print(f"No definitions found for {selected_word}")
        return
    output_components.append(_get_word_string(word))

    if not word.sentences:
        print(f"No example sentences found for {selected_word}")
    else:
        output_components.append(_get_sentence_string(word))

    separator = "-" * 70
    print(separator, '\n\n'.join(output_components), separator, sep='\n')

if __name__ == "__main__":
    main()
