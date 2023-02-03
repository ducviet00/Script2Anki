from random import randrange
import genanki


def create_note(model):
    note = genanki.Note(
        guid=randrange(1 << 30, 1 << 31),
        fields=[
            "random",
            "ngẫu nhiên",
            "r___om",
            "abcxyz",
            "noun",
            "random.random",
            "xx",
            "transciption",
        ],
        model=model,
        tags=["prettify", "prettify:2"],
    )
    return note


def create_notes():
    pass
