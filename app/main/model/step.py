from sqlalchemy_serializer import SerializerMixin

from .. import db


class BrewStep(db.Model, SerializerMixin):
    __tablename__ = 'brew_step'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    index = db.Column(db.Integer)
    started = db.Column(db.DateTime(timezone=True))
    ended = db.Column(db.DateTime(timezone=True))

    # def __init__(self, parent_id, name, index):
    #     self.parent_id = parent_id
    #     self.name = name
    #     self.index = index
