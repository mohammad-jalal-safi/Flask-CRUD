from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, login_required, logout_user
from forms.form_user_management import LoginForm, SignupForm
from models.user_model import User

from server import db
from services.utils import main_bp

@main_bp.route('/signup', methods=['GET', 'POST'])
@login_required
def signup():
    try:
        form = SignupForm()
        if form.validate_on_submit():
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user is None:
                user = User(
                    name=form.name.data,
                    email=form.email.data,
                )
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()  # Create new user
                login_user(user)  # Log in as newly created user
                return redirect(url_for('main_bp.login'))
            flash('A user already exists with that email address.')
        return render_template(
            'signup.jinja2',
            title='Create an Account.',
            form=form,
            template='signup-page',
            body="Sign up for a user account."
        )
    except:
        return 1


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main_page'))

        form = LoginForm()
        # Validate login attempt
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(password=form.password.data):
                login_user(user)
                return redirect(url_for('main_bp.main_page'))
            flash('Invalid username/password combination')
            return redirect(url_for('main_bp.login'))
        return render_template(
            'login.jinja2',
            form=form,
            title='Log in.',
            template='login-page',
            body="Log in with your User account."
        )
    except:
        return 1

@main_bp.route("/logout")
@login_required
def logout():
    try:
        """User log-out logic."""
        logout_user()
        return redirect(url_for('main_bp.login'))
    except:
        return 1