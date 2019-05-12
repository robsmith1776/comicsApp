from flask import Flask, url_for, render_template
from .functions import get_html
from .db import run_insert

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/comics/")
@app.route("/comics/<delete>/")
def comics(delete=None):
    comic_list = get_html()
    run_insert(comic_list, delete)
    return render_template("comics.html", comic_list=comic_list, delete=delete)


@app.route("/user/")
@app.route("/user/<username>/")
def show_user_profile(username=None):
    # show the user profile for that user
    name = username or "Have My By Back"
    return render_template("user.html", name=name)

# python -m flask run
