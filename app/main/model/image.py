from sqlalchemy_serializer import SerializerMixin

from .. import db


class Image(db.Model, SerializerMixin):
    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('brew.id'))
    url = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    # size? mime? other?
    # step relation?

    def __repr__(self):
        return "<Image '{}'>".format(self.url)
