import pykakasi

from constants import Constants

class ExampleSentence:
    def __init__(self, jpn_sentence, eng_sentence):
        self.jpn = jpn_sentence
        self.eng = eng_sentence
        self.jpn_kana = self._get_kana(self.jpn)

    def _get_kana(self, sentence: str) -> str:
        kks = pykakasi.kakasi()
        return Constants.WIDE_SPACE.join(
            [item['hira'] for item in kks.convert(sentence)]
        )
