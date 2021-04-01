import datetime
import jsons
from typing import List
from app.main import db
from app.main.model.brew import Brew, BrewStep


def save_brew(data):

    # TODO: find a better way to deserialize nested values
    brew = jsons.load(data, Brew)
    if "brew_steps" in data:
        brew.brew_steps = jsons.load(data["brew_steps"], List[BrewStep])

    if "id" not in data:
        brew.created = datetime.datetime.utcnow()
        # TODO:
        # steps: opvarmning, mæskning, eftergydning, urtkogning, urtkøling
        create(brew)
        return brew.to_dict(), 201
    else:
        update(brew)
        return brew.to_dict(), 200


def get_all_brews():
    return Brew.query.all()


def get_a_brew(id):
    return Brew.query.filter_by(id=id).first()


def create(data):
    db.session.add(data)
    db.session.commit()

def update(data):
    db.session.merge(data)
    db.session.commit()
