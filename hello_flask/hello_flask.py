'''
Adapted from the tutorial here:
http://pymbook.readthedocs.org/en/latest/flask.html

will be changing this to follow this Flaskr tutorial:
    http://flask.pocoo.org/docs/0.10/tutorial/

'''

import flask
from flask import request, url_for

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    ''' Displays the index page accessible at '/' '''
    return flask.render_template('index.html')

def log_user_in(usrname):
    '''
    Allows the user to login.  Validation must be done
    before this is called!
    '''
    return flask.render_template('hello.html', name=usrname)


def valid_login(usrname, passwd):
    # this ignores all hashing requirements to keep this simple
    return usrname == 'jdoe' and passwd == 'letmein'  # ignoring any DB here..


@APP.route('/login', methods=['GET', 'POST'])
def login():
    error_msg = None
    if request.method == 'POST':
        # handle login here
        usrname = request.form['usrname']
        passwd = request.form['passwd']
        if valid_login(usrname, passwd):
            return log_user_in(usrname)
        else:
            error_msg = 'Invalid username/password!'

    return flask.render_template('login.html', error_msg=error_msg)

if __name__ == '__main__':
    APP.debug = True
    APP.run()
