from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/home")
def home():
    return "Home Page"

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# URL BUILDING
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

"""
The canonical URL for the projects endpoint has a trailing slash. 
It’s similar to a folder in a file system. 
If you access the URL without a trailing slash (/projects), 
Flask redirects you to the canonical URL with the trailing slash (/projects/).

The canonical URL for the about endpoint does not have a trailing slash. 
It’s similar to the pathname of a file. 
Accessing the URL with a trailing slash (/about/) produces a 404 “Not Found” error. 
This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
"""

@app.route('/projects/') # Trailing slash
def projects():
    return 'The project page'

@app.route('/about') # No trailing slash
def about():
    return 'The about page'