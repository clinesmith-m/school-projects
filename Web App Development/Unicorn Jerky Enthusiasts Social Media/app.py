# Run with:
# FLASK_ENV=development flask run --host=0.0.0.0

from flask import abort, Flask, json, redirect, render_template, request,\
    Response, url_for, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import uuid

UPLOADS_DIR = 'static/img/uploads'
THUMBNAILS_DIR = 'static/img/thumbnails'

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)

from models import User, Post, db
from forms import AddPostForm, SignUpForm, SignInForm, AboutUserForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/posts/', methods=['GET'])
def fuck_self():
    if session['user_available']:
        blogpost = AddPostForm(request.form)
        posts = Post.query.order_by(Post.pid.desc()).limit(10).all()
        user = User.query.all()
        return render_template('porn.html', blogpost=blogpost, posts=posts, user=user)
    flash('User is not Authenticated')
    return redirect(url_for('index'))

@app.route('/api/posts/', methods=['POST'])
def kill_self():
    if session['user_available']:
        blogpost = AddPostForm(request.form)
        us = User.query.filter_by(username=session['current_user']).first()
        if request.method == 'POST':
            infile = request.files['imagefile']
            if infile:
                filename = secure_filename(infile.filename)
                randname = str(uuid.uuid4())
                filename = randname + filename
                filepath = os.path.join(UPLOADS_DIR, filename)
                infile.save(filepath)
            else:
                filepath = None

            
            bp = Post(title=request.form['title'], description=request.form['posttext'], imgpath=filename, puid=us.uid)
            db.session.add(bp)
            db.session.commit()
            return redirect(url_for('fuck_self'))
    flash('User is not Authenticated')
    return redirect(url_for('index'))

@app.route('/delete/<int:pid>/', methods=(['GET', 'DELETE']))
def kill_post(pid):
    me = Post.query.filter(Post.pid == pid).first()
    post_owner = me.puid
    
    us = User.query.filter_by(username=session['current_user']).first()
    curr_usr = us.uid

    if post_owner == curr_usr:
        db.session.delete(me)
        db.session.commit()
        flash('It gone.')
        return redirect(url_for('fuck_self'))
    else:
        flash('You\'re not my dad! (Invalid user to delete this post)')
        return redirect(url_for('fuck_self'))
    

@app.route('/api/signup/', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        # Textual data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Profile pic
        infile = request.files['profilepic']
        filename = secure_filename(infile.filename)
        randname = str(uuid.uuid4())
        filename = randname + filename
        filepath = os.path.join(THUMBNAILS_DIR, filename)
        infile.save(filepath)
        # Sign them in
        current_user = log.username
        session['current_user'] = current_user
        session['user_available'] = True
        # Send it
        reg = User(firstname, lastname, username, password, email, filepath)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('fuck_self'))
    return render_template('signup.html', signupform=signupform)


@app.route('/api/signin/', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if request.method == 'POST':
        em = signinform.email.data
        log = User.query.filter_by(email=em).first()
        if log.password == signinform.password.data:
            current_user = log.username
            session['current_user'] = current_user
            session['user_available'] = True
            return redirect(url_for('fuck_self'))
    return render_template('signin.html', signinform=signinform)


@app.route('/api/about_user/')
def show_user():
    aboutuserform = AboutUserForm()
    if session['user_available']:
        user = User.query.filter_by(username=session['current_user']).first()
        return render_template('about_user.html', user=user, aboutuserform=aboutuserform)
    flash('You are not a Authenticated User')
    return redirect(url_for('index'))


@app.route('/api/logout/')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('index'))


@app.route('/blog/api/v0.1/posts', methods=['GET'])
def get_tasks():
    posts = Post.query.all()
    """for i in api_posts:
        title= i.title
        description = i.description
        data_dict= {'title': title, 'description': description}"""
    """for i in posts:
        t[i] = posts.title
    print(t)"""
    title = posts.title
    print(title)
    description = posts.description
    return jsonify(title=title, description=description)


if __name__ == '__main__':
    app.run()

