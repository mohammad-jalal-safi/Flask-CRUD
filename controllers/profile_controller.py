from flask_login import login_required

from main_module import app
from flask import render_template , request , redirect , url_for
import services.profile_services as prs
import services.lookup_services as lookups
from models.profile_model import Profile
from services.utils import main_bp



genders = lookups.get_genders()

@main_bp.route('/search', methods=["GET", "POST"])
@login_required
def search():
    try:
        profiles = []
        if request.method == "POST":
            name = request.form["name"]
            profiles = prs.search_profile(name)
        return render_template('profile.html',datas=profiles,genders = genders)
    except:
        return 1

@main_bp.route('/save' , methods=["GET", "POST"])
@login_required
def save():
    try:
        if request.method == "POST":
            name = request.form["name"]
            last_name = request.form["last_name"]
            father_name = request.form["father_name"]
            grand_father_name = request.form["grand_father_name"]
            phone = request.form["phone"]
            gender_id= request.form["gender_id"]
            profile = Profile(name = name, last_name=last_name,father_name = father_name,grand_father_name=grand_father_name,
                              phone=phone,gender_id = gender_id)
            prs.save(profile)
        return redirect(url_for("main_bp.search"))
    except:
        return 1


@main_bp.route('/update/<int:id>', methods=["GET"])
@login_required
def update(id):
    try:
        profile = prs.get_profile_by_id(id)
        return render_template('profile_update.html', profile=profile,genders = genders)
    except:
        return 1

@main_bp.route('/update', methods=['POST'])
@login_required
def update_profile():
    id= request.form["id"]
    name = request.form["name"]
    last_name = request.form["last_name"]
    father_name = request.form["father_name"]
    grand_father_name = request.form["grand_father_name"]
    phone = request.form["phone"]
    gender_id = request.form["gender_id"]
    profile = Profile(id=id, name=name, last_name=last_name, father_name=father_name, grand_father_name=grand_father_name,
                      phone=phone, gender_id=gender_id)
    prs.update(profile)
    return redirect(url_for("main_bp.search"))

@main_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    try:
        prs.delete(id)
        return redirect(url_for("main_bp.search"))
    except:
        return 1