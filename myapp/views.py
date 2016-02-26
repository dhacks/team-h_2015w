from datetime import datetime

from flask import render_template, flash, url_for, redirect, request
from flask.ext.login import login_user, logout_user, login_required, current_user

from myapp import app, db
from myapp.forms import LoginForm, SignupForm, PostForm, CommentForm, SearchForm
from myapp.models import User, Post, Comment


@app.route('/', methods=('GET', 'POST'))
def index():
    posts = Post.query.order_by(Post.published_on)
    form = SearchForm()

    if request.method == 'POST':
        tag = form.tag.data
        print(tag)
        posts = Post.query.filter_by(tag=tag)  # .order_by(Post.published_on)
        return render_template('main.html', form=form, posts=posts)

    return render_template('main.html', posts=posts, form=form)


@app.route('/<int:post_id>')
def page(post_id):
    article = Post.query.get(post_id)
    return render_template('page.html', page=article)


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Thanks, you are registered')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.verify_password(form.password.data):
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
    form = PostForm()
    if form.validate_on_submit():
        article = Post(title=form.title.data, author=current_user, tag=form.tag.data, body=form.body.data, published_on=datetime.now())
        db.session.add(article)
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
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(author=current_user, post_on=datetime.now(), body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        print("comment post success")
        return redirect(url_for('post_main'))

    return render_template('editor.html', form=form)
