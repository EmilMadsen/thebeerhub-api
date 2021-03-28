from sqlalchemy_serializer import SerializerMixin

from .. import db


class Brew(db.Model, SerializerMixin):
    __tablename__ = "brew"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brew_name = db.Column(db.String(255), nullable=False)
    brew_type = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    brewsters = db.Column(db.String(255))
    location = db.Column(db.String(255))
    recipe = db.Column(db.String(255))
    brew_steps = db.relationship("BrewStep")
    target_start_gravity = db.Column(db.Integer)
    actual_start_gravity = db.Column(db.Integer)
    target_end_gravity = db.Column(db.Integer)
    actual_end_gravity = db.Column(db.Integer)

    # fermentation_logs = db.Column(db.String(255))
    # pictures = db.Column(db.String(255))

    def __repr__(self):
        return "<Brew '{}'>".format(self.brew_name)


class BrewStep(db.Model, SerializerMixin):
    __tablename__ = 'brew_step'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    name = db.Column(db.String(255))
    index = db.Column(db.Integer)
    started = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)

