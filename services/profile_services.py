from models.gender_model import Gender
from models.profile_model import Profile
from server import db

def search_profile(name):
    return Profile.query\
        .join(Gender,Profile.gender_id == Gender.id)\
        .add_columns(Profile.name,Profile.last_name,Profile.father_name,Profile.grand_father_name,Profile.phone,Profile.gender_id,Profile.id,Gender.title).filter(Profile.name.ilike('%'+name+'%')).all()

def get_profile_by_id(id):
    return Profile.query.get(id)

def save(profile):
    db.session.add(profile)
    db.session.commit()

def update(data):
    profile = get_profile_by_id(data.id)
    profile.name = data.name
    profile.last_name = data.last_name
    profile.father_name = data.father_name
    profile.grand_father_name = data.grand_father_name
    profile.phone = data.phone
    profile.gender_id = data.gender_id
    db.session.commit()

def delete(id):
    Profile.query.filter_by(id=id).delete()
    db.session.commit()