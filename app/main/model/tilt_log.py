from sqlalchemy_serializer import SerializerMixin

from .. import db


class TiltLog(db.Model, SerializerMixin):
    __tablename__ = "tilt_log"

    id = db.Column(db.String(255), primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<TiltLog '{}'>".format(self.id)
