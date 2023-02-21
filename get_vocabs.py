import nltk
import pysubs2
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from wordfreq import zipf_frequency

word_dict = set(words.words())
lemmatizer = WordNetLemmatizer()

tag_map = {
    "ADJ": "a",
    "ADV": "r",
    "NOUN": "n",
    "VERB": "v"
}


def get_vocabs(filepath: str, freq_lo: float, freq_up: float):
    if filepath.endswith("srt"):
        texts = pysubs2.load(filepath, encoding="utf-8")
        texts = [line.plaintext.strip() for line in texts]
    else:
        with open(filepath, "r") as f:
            texts = f.readlines()
            texts = [line.strip() for line in texts]

    vocabs = []
    for line in texts:
        text = [w.lower() for w in nltk.word_tokenize(line) if w.isalpha()]
        pos_tag = nltk.pos_tag(text, tagset='universal')

        for word, tag in pos_tag:
            word_stem = lemmatizer.lemmatize(word, pos=tag_map.get(tag, "n"))
            if word_stem not in word_dict:
                continue
            freq = zipf_frequency(word_stem, "en")
            if freq_lo < freq < freq_up:
                vocabs.append(word_stem)

    return set(vocabs)
