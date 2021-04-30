import datetime
import jsons
from typing import List
from app.main import db
from app.main.model.brew import Brew
from app.main.model.image import Image
from app.main.service.step_service import initialize_steps, delete_steps_by_parent_id


def save_brew(data):

    # TODO: find a better way to deserialize nested values
    brew = jsons.load(data, Brew)
    if "brew_steps" in data:
        brew.images = jsons.load(data["images"], List[Image])

    if "id" not in data:
        brew.created = datetime.datetime.utcnow()
        create(brew)
        initialize_steps(brew.id)
        return brew, 201
    else:
        update(brew)
        return brew, 200


def get_all_brews():
    return Brew.query.order_by(Brew.created.desc()).all()


def get_all_tiltable_brews():
    return Brew.query.filter(Brew.tilt_url != None).all()


def get_a_brew(id):
    return Brew.query.filter_by(id=id).first()


def delete_a_brew(id):
    delete_steps_by_parent_id(id)
    db.session.query(Brew).filter(Brew.id == id).delete()
    db.session.commit()
    return None


def create(data):
    db.session.add(data)
    db.session.commit()


def update(data):
    db.session.merge(data)
    db.session.commit()
