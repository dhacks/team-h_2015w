from myapp import app, db
from flask import render_template, flash, url_for, redirect, request
from flask.ext.login import login_user, logout_user, login_required
from myapp.forms import Login, Signup
from myapp.models import User, Article


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = Signup(request.form)
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data,
                    password=form.pswd1.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks, you are registered')
        return redirect(url_for('main'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.verify_password(form.pswd.data):
            login_user(user)
            print('login success!')

            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/post')
def post():
    #return render_template("editor.html")
    return "post page"

@app.route('/hoge')
@login_required
def hoge():
    return 'You are logged in!'