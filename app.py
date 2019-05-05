from flask import Flask, url_for, render_template
from .functions import get_html
from .db import run_insert

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/comics/')
def comics():
    comic_list = get_html()
    run_insert(comic_list)
    return render_template('comics.html', comic_list=comic_list)


@app.route('/user/')
@app.route('/user/<username>/')
def show_user_profile(username=None):
    # show the user profile for that user

    thisthing = username or 'Have My By Back'

    print(url_for('comics', username='John Doe'))
    return render_template('user.html', thisthing=thisthing)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
# python -m flask run
