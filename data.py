from csv import DictReader
from lxml import etree

class Data:
    def __init__(self, *, jmdict_path, tsuneyo_path):
        self.jmdict = self._init_jmdict(jmdict_path)
        self.tsuneyo = self._init_tsuneyo(tsuneyo_path)

    def _init_jmdict(self, path: str):
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
