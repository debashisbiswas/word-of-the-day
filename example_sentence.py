from pykakasi import kakasi

from constants import Constants

class ExampleSentence:
    def __init__(self, jpn_sentence, eng_sentence):
        self.jpn = jpn_sentence
        self.eng = eng_sentence
        self.jpn_kana = self._get_kana(self.jpn)

    def _get_kana(self, sentence: str) -> str:
        kks = kakasi()
        converted_tokens = []
        for token in kks.convert(sentence):
            # Hiragana and katakana are not converted.
            # Kanji is converted to hiragana.
            new_token = token['orig']
            if token['orig'] not in (token['hira'], token['kana']):
                new_token = token['hira']
            converted_tokens.append(new_token)

        return Constants.FULL_WIDTH_SPACE.join(converted_tokens)
