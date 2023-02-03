from random import randrange
import genanki


def create_model():
    with open("card-template/front.html", "r+") as f:
        front_html = f.read()
    with open("card-template/back.html", "r+") as f:
        back_html = f.read()
    with open("card-template/front-reverse.html", "r+") as f:
        rfront_html = f.read()
    with open("card-template/back-reverse.html", "r+") as f:
        rback_html = f.read()
    with open("card-template/style.css", "r+") as f:
        css = f.read()

    templates = [
        {
            "name": "Card 1",
            "qfmt": front_html,
            "afmt": back_html,
        },
        {
            "name": "Card 2",
            "qfmt": rfront_html,
            "afmt": rback_html,
        },
    ]
    fields = [
        "target-word",
        "vietnamese",
        "suggestion",
        "explanation",
        "word-type",
        "example",
        "pronouncing",
        "transcription",
    ]
    model_fields = [{"name": field} for field in fields]

    model = genanki.Model(
        model_id=randrange(1 << 30, 1 << 31),
        name="Prettify Model",
        fields=model_fields,
        templates=templates,
        css=css,
        model_type=genanki.Model.FRONT_BACK,
    )

    return model


create_model()
