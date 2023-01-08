from flask import Blueprint
from flask import redirect, render_template
import os

route = Blueprint('index', __name__)


@route.route("/")
def index():
    print(os.environ.get('SECRET_KEY'))
    print(os.environ.get('URI'))
    return render_template("index.html")


