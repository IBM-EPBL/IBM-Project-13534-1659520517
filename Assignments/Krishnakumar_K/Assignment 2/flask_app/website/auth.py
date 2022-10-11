from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
            email =request.form.get('email')
            password=request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                else:
                    flash('Incorrect password',category='error')
            else:
                flash('Email not exist', category='error')
    return render_template("index.html")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Name = request.form.get('Name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email alrady exist', category='error')
        elif len(Name) <1:
            flash('Name must be greater than 1 character', category='error')
        elif len(email) < 1:
            flash('email must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('password doesn\'t match', category='error')
        else:
            new_user = User(Name=Name, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("registration.html")

