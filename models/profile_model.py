from server import db

class Profile(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    father_name = db.Column(db.String(255),nullable=False)
    grand_father_name = db.Column(db.String(255),nullable=False)
    phone = db.Column(db.String(255),nullable=True)
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'),nullable=False)

