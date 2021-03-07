import datetime

from app.main import db
from app.main.model.brew import Brew


def save_brew(data):
    if "id" not in data:
        new_brew = Brew(
            brew_name=data['brew_name'],
            brew_type=data['brew_type'],
            datetime=datetime.datetime.utcnow()
        )
        save_changes(new_brew)
        return new_brew.to_dict(), 201
    else:
        existing = Brew.query.get(data['id'])
        existing.brew_name = data['brew_name']
        existing.brew_type = data['brew_type']
        save_changes(existing)
        return existing.to_dict(), 200


def get_all_brews():
    return Brew.query.all()


def get_a_brew(id):
    return Brew.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()