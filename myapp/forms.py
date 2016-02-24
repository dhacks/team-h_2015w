from myapp import app
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Required, Email, EqualTo


class Signup(Form):
    username = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required(),Email()])
    pswd1 = PasswordField('Create a password',)
    pswd2 = PasswordField('Confirm your password', validators=[EqualTo(pswd1)])


class Login(Form):

    email = StringField(validators=[Required(),Email()])
    pswd = PasswordField()

