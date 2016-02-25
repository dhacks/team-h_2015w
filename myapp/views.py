from datetime import datetime

from flask import render_template, flash, url_for, redirect, request
from flask.ext.login import login_user, logout_user, login_required, current_user

from myapp import app, db
from myapp.forms import Login, Signup, Post_Form, Comment_Form
from myapp.models import User, Post, Comment


@app.route('/')
def index():
    posts = Post.query.order_by(Post.published_on)

    return render_template('main.html', posts=posts)


@app.route('/<int:postid>')
def page(postid):
    page = Post.query.get(postid)
    return render_template('page.html', page=page)


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = Signup(request.form)
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data,
                    password=form.pswd1.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks, you are registered')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.verify_password(form.pswd.data):
            login_user(user)
            print('login success!')
            return redirect(url_for('index'))
        else:
            print('login failed ><')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """
    ログインページ
    """
    logout_user()
    return redirect(url_for('index'))


@app.route('/post', methods=('GET', 'POST'))
@login_required
def post():
    """
    記事をポストするページ
    """
    form = Post_Form()
    if form.validate_on_submit():
        post = Post(title=form.title.data, author_id=current_user.get_id(), tag=form.tag.data,
                    body=form.body.data, published_on=datetime.now())
        db.session.add(post)
        db.session.commit()
        print("post success")
        flash('Successfully posted')
        return redirect(url_for('index'))
    return render_template('post.html', form=form)


@app.route('/post_comment', methods=('GET', 'POST'))
# @login_required
def post_comment():
    """
    本文表示、個別ページ post_idから対応するPOSTのデータをDBからとって表示
    本文したにコメント表示
    """
    form = Comment_Form()
    if form.validate_on_submit():
        cmmnt = Comment(poster_name=current_user.name, post_on=datetime.now(), cbody=form.cbody.data)
        db.session.add(cmmnt)
        db.session.commit()
        print("comment post succenss")
        return redirect(url_for('post_main'))

    return render_template('editor.html', form=form)
