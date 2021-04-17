import datetime

import jsons
from app.main import db
from app.main.model.step import BrewStep


def initialize_steps(parent_id):

    # link each step to the next.
    step = BrewStep(parent_id=parent_id, name='urtkøling', index=6)
    create(step)
    step = BrewStep(parent_id=parent_id, name='urtkogning', next_step=step.id, index=5)
    create(step)
    step = BrewStep(parent_id=parent_id, name='opkogning', next_step=step.id, index=4)
    create(step)
    step = BrewStep(parent_id=parent_id, name='eftergydning', next_step=step.id, index=3)
    create(step)
    step = BrewStep(parent_id=parent_id, name='mæskning', next_step=step.id, index=2)
    create(step)
    create(BrewStep(parent_id=parent_id, name='opvarmning', next_step=step.id, index=1))


def update_step(data):
    step = jsons.load(data, BrewStep)
    update(step)
    return step, 200


def get_steps_by_parent_id(parent_id):
    return BrewStep.query.filter_by(parent_id=parent_id).order_by(BrewStep.index).all()


def get_step_by_id(id_):
    return BrewStep.query.filter_by(id=id_).first()


def get_current_active_step(parent_id):
    # find where step is started, but not ended yet.
    # assume sorted by query.
    steps = get_steps_by_parent_id(parent_id)
    for step in steps:
        if step.ended is None:
            return step

    return None


def go_to_next_step(parent_id):

    step = get_current_active_step(parent_id)

    if step is not None:
        if step.started is None:
            # first step (not started yet)
            step.started = datetime.datetime.utcnow()
            update(step)
            return step
        elif step.ended is None:
            # end current active & start next
            step.ended = datetime.datetime.utcnow()
            update(step)
            next_step = get_step_by_id(step.next_step)
            if next_step is not None:
                next_step.started = datetime.datetime.utcnow()
                update(next_step)
                return next_step

    return None


def delete_steps_by_parent_id(parent_id):
    BrewStep.query.filter_by(parent_id=parent_id).delete()
    db.session.commit()


def create(data):
    db.session.add(data)
    db.session.commit()


def update(data):
    db.session.merge(data)
    db.session.commit()
