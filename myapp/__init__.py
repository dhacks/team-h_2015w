from flask import Flask, g
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect
from flask.ext.login import LoginManager
from flaskext.markdown import Markdown

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'main.db')
manager = Manager(app)
db = SQLAlchemy(app)
#Flask-Migrate
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
#Flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.uid == int(user_id)).first()

#Flask-WTF
app.secret_key = 'hogehoge'
CsrfProtect(app)
#Flask-Bootstrap
Bootstrap(app)
#Flask-Markdown
Markdown(app)

######################################################
def getdb():
    return db
def getapp():
    return app


from myapp import views, models
