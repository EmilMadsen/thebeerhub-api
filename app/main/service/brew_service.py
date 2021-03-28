import datetime
import jsons

from app.main import db
from app.main.model.brew import Brew


def save_brew(data):
    brew = jsons.load(data, Brew)
    print(brew)

    if "id" not in data:
        brew.created = datetime.datetime.utcnow()
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
