from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class SignupForm(Form):
    username = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password')
    password_confirm = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Signup')


class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password')
    submit = SubmitField('Login')


class PostForm(Form):
    title = StringField('Title', validators=[InputRequired()])
    tag = StringField('Tag')
    body = TextAreaField('Body', validators=[InputRequired()])
    submit = SubmitField('Post')


class CommentForm(Form):
    body = TextAreaField('comment body', validators=[InputRequired()])


class SearchForm(Form):
    tag = StringField('tag')
    submit = SubmitField('検索')
