from server import db

class Gender(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    profiles = db.relationship('Profile', backref='profile', lazy=True)