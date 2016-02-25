from myapp import app, db
from flask import render_template, flash, url_for, redirect, request
from flask.ext.login import login_user, logout_user, login_required, current_user
from myapp.forms import Login, Signup, Post_Form
from myapp.models import User, Post


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
            print('login failed ><')
            return redirect(url_for('login'))

    return render_template('login.html',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/post',methods=('GET','POST'))
@login_required
def post():
    form = Post_Form()
    if form.validate_on_submit():
        post = Post(title=form.title.data, author_id= current_user.get_id ,tag = form.tag.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        print("post success")
        flash('Successfully posted')
        return redirect(url_for('main'))
    return render_template('post.html', form=form)

@app.route('/hoge')
@login_required
def hoge():
    #login check
    return 'You are logged in!'