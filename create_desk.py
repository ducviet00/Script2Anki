from random import randrange
import genanki

from create_model import create_model
from create_notes import create_notes


def create_desk(desk_name):
    model = create_model()
    notes = create_notes()
    deck = genanki.Deck(
        desk_id=randrange(1 << 30, 1 << 31),
        name=f"{desk_name}",
        description="",
    )
    deck.add_model(model)
    for note in notes:
        deck.add_note(note)
    genanki.Package(deck).write_to_file(f"{desk_name}.apkg")
