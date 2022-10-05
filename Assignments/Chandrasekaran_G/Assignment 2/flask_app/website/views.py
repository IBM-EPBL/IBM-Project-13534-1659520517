from flask import Blueprint, render_template

views = Blueprint('views',__name__)


@views.route('/')
@views.route('/home', methods=['GET','POST'])
def home():
    return render_template("welcome.html")