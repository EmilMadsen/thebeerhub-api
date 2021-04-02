import jsons
from app.main import db
from app.main.model.step import BrewStep


def initialize_steps(parent_id):
    create(BrewStep(parent_id=parent_id, name='opvarmning', index=1))
    create(BrewStep(parent_id=parent_id, name='mæskning', index=2))
    create(BrewStep(parent_id=parent_id, name='eftergydning', index=3))
    create(BrewStep(parent_id=parent_id, name='urtkogning', index=4))
    create(BrewStep(parent_id=parent_id, name='urtkøling', index=5))


def update_step(data):
    step = jsons.load(data, BrewStep)
    update(step)
    return step.to_dict(), 200


def get_steps_by_parent_id(parent_id):
    return BrewStep.query.filter_by(parent_id=parent_id).all()


def delete_steps_by_parent_id(parent_id):
    BrewStep.query.filter_by(parent_id=parent_id).delete()
    db.session.commit()


def create(data):
    db.session.add(data)
    db.session.commit()


def update(data):
    db.session.merge(data)
    db.session.commit()
