from models.gender_model import Gender
def get_genders():
    return Gender.query.all()