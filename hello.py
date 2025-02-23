from flask import Flask, url_for, request, render_template
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



# HTTP METHODS
# Get: Non-secure (in address bar)
# Post: Secure (passwords)


# To - Do
# 1. Define 'valid login'
# 2. Define 'do the login'
# 3 Define 'show_the_login_form'

# Notes
# Request Documentation: https://flask.palletsprojects.com/en/stable/api/#flask.Request
# Recommend accessing URL parameters with get or by catching the KeyError because users might change the URL and presenting them a 400 bad request page in that case is not user friendly.
@app.route('/login', methods=['GET', 'POST'])
def login():
    render_template('logInOrSignUp.html') # Flask will look for templates in the templates folder!
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return do_the_login() # Logins in user
    else:
        return show_the_login_form() # Prompts login form
# Both of the functions above need to be written im just following the documentation

@app.route('/userLoginVerification', methods=['GET', 'POST'])
def userLoginVerification(username, password):
    pass

@app.route('/signUp')
def signUp():
    pass

