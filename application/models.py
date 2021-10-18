from application.database import db
import uuid

class Contestant(db.Model):
    id = db.Column(db.String(80), primary_key=True, default=lambda : str(uuid.uuid4()))
    name = db.Column(db.String(80), nullable=False)
    costumeTitle = db.Column(db.String(120), nullable=False)
    costumeImgUrl = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Contestant %r>' % self.name
# db.create_all()