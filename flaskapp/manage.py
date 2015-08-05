#! /usr/bin/env python
import os

from flask.ext.script import Manager, Shell, Command

from flaskapp import create_app, db
from flaskapp.models import Cookie

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


class DBInit(Command):
    ''' Creates tables from SQLAlchemy models. '''

    def __init__(self, db):
        self.db = db

    def run(self):
        self.db.create_all()

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db_init', DBInit(db))

if __name__ == '__main__':
    manager.run()
