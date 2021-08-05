from lxml import etree

from data import Data
from example_sentence import ExampleSentence

class Word:
    def __init__(self, word: str, *, data: Data):
        self.word = word
        self.data = data
        self.reading = self._get_reading()
        self.pitch = self._get_pitch()
        self.definitions = self._get_definitions()
        self.sentences = self._get_sentences()

    def _get_reading(self) -> str:
        custom_dict = self.data.tsuneyo
        return custom_dict[self.word]['kana'] if self.word in custom_dict else ''
    
    def _get_pitch(self) -> int:
        custom_dict = self.data.tsuneyo
        return custom_dict[self.word]['accent'] if self.word in custom_dict else -1

    def _get_definitions(self) -> str:
        path = f"//keb[text()='{self.word}']/ancestor::entry/sense/gloss | //reb[text()='{self.word}']/ancestor::entry/sense/gloss"
        element: list[etree._Element] = self.data.jmdict.xpath(path)

        return [gloss.text for gloss in element]

    def _get_sentences(self) -> list[ExampleSentence]:
        path = f"//keb[text()='{self.word}']/ancestor::entry/sense/example | //reb[text()='{self.word}']/ancestor::entry/sense/example"
        examples: list[etree._Element] = self.data.jmdict.xpath(path)
        sentences: list[ExampleSentence] = []
        for example in examples:
            jpn = example.xpath("ex_sent[@xml:lang='jpn']")[0].text
            eng = example.xpath("ex_sent[@xml:lang='eng']")[0].text
            sentences.append(ExampleSentence(jpn, eng))
        return sentences
