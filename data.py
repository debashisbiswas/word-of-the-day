from csv import DictReader
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
            reader = DictReader(tsv, delimiter="\t", quotechar='"')
            for row in reader:
                custom_dict[row['word']] = {
                    "kana": row['kana'],
                    "accent": row['accent']
                }
        return custom_dict
