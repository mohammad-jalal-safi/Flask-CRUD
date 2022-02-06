from main_module import app
from flask import render_template , request , redirect , url_for
from flask_login import login_required
from services.utils import main_bp

@main_bp.route('/')
@login_required
def main_page():
    return render_template('main_page.html')