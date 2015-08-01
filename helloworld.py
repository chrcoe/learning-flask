from flask import Flask, url_for
app = Flask(__name__)


@app.route("/")
def index():
    # this does not work as I had intended .. prints to console not screen,
    # doh!
    print('Index page')
    print(url_for('hello'))
    print(url_for('show_user_profile', usrname='jdoe'))
    return 'Index Page'


@app.route("/hello")
def hello():
    return 'Hello World!'


@app.route('/user/<usrname>')
def show_user_profile(usrname):
    return 'Username {}'.format(usrname)

if __name__ == "__main__":
    debug_flag = True
    app.run(debug=debug_flag)
