from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class SignupForm(Form):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Create a password', )
    password_confirm = PasswordField('Confirm your password', validators=[EqualTo(password)])


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField()
    submit = SubmitField('submit')


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    tag = StringField('tag')
    body = TextAreaField('body', validators=[DataRequired()])
    submit = SubmitField('submit')


class CommentForm(Form):
    body = TextAreaField('comment body', validators=[DataRequired()])


class SearchForm(Form):
    tag = StringField('tag')
    submit = SubmitField('検索')
