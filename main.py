import MeCab


class Mecab:
    def __init__(self, sentence):
        self.sentence = sentence
        self.t = MeCab.Tagger()
        self.wakati = MeCab.Tagger("-Owakati")

    def print_parse(self):
        print(self.t.parse(self.sentence))

    def parsed_list(self):
        return self.wakati.parse(self.sentence).split()


sentence = "ボイスピンクは完全なオンライン写真を有するトータルソリューションサービスです。ボイスピンクはリモートチームの生産性とエンディ地面と。"

dictionaries = [
    {"f": "ボイスピンク", "t": "VoicePing"},
]


def simple_replace(sentence, dict):
    for d in dict:
        sentence = sentence.replace(d["f"], d["t"])
    return sentence


if __name__ == "__main__":
    print(sentence)

    replaced_sentence = simple_replace(sentence, dictionaries)
    print(replaced_sentence)

    mecab = Mecab(replaced_sentence)
    mecab_list = mecab.parsed_list()
    print(mecab_list)
