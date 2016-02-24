from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from myapp import db
from . import login_manager

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()


class User(UserMixin, db.Model):
    """
    とりあえず、ユーザーの名前とメアドとパスワード（ハッシュ後）
    回生、学部、等々は略
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # USER ID, PRIMARY

    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)

    year = db.Column(db.Integer)

    user_id = db.relationship('Post', backref='user')

    password_hash = db.Column(db.String(128))

    def __init__(self,username,email,password):#,year):
        self.username = username
        self.email = email
        self.year = 1
        self.password = password


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
        パスワード　ハッシュ化
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        ハッシュ化（パスワード（生）） == バスワード（ハッシュ）
        -> True
        """
        return check_password_hash(self.password_hash, password)

#    def is_active(self):
#        """True, as all users are active."""
#        return True
#
#    def get_id(self):
#        """Return the email address to satisfy Flask-Login's requirements."""
#        return self.email
#
#    def is_authenticated(self):
#        """Return True if the user is authenticated."""
#        return self.authenticated
#
#    def is_anonymous(self):
#        """False, as anonymous users aren't supported."""
#        return False



class Post(db.Model):
    """
    本文記事　まわり
    """
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)  # :POST ID, PRIMARY

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(512))
    tag = db.Column(db.String(32))
    body = db.Column(db.Text)
    published_on = db.Column(db.DateTime)

    def __init__(self,title,tag,body):
        self.author_id = 0
        self.title = title
        self.tag = tag
        self.body = body
        self.published_on = datetime.now()


