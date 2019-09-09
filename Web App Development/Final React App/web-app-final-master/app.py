from flask import abort, Flask, json, redirect,\
	render_template, request, Response, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)


# Import any SQLAlchemy model classes you wish.
from models import User, Post, Image


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/<string:tag>')
def find_tagged_posts(tag):
	images = list(map( lambda i: i.serialize(),Image.query.filter(Image.tags.find(tag) != 0)))
	for image in images:
		try:
			image['tags'] = image['tags'].split(",")
		except:
			pass
	return jsonify(images)



def img_validate(infile):
	filename = secure_filename(infile.filename)
	type_index = filename.find('.')
	if filename[type_index:] == ".jpg" or filename[type_index:] == ".png":
		return True
	return False

def min_validate():
	date = request.form['date']
	slash_index = date.find("/")
	if slash_index == 2:
		try:
			month = int(date[:2])
			year = int(date[3:])
			if month - 12 <= 0:
				return True
		except:
			return False
	return False

@app.route('/', methods=["POST"])
def make_post():
	if request.method == 'POST':
		imgfile = request.files["imagefile"]
		#minfile = request.files['minfile']
		#constfile = request.files['constitution']
		#us = User.query.filter_by(username=session['current_user']).first()
		if imgfile:
			if img_validate(imgfile):
				filename = secure_filename(infile.filename)
				randname = str(uuid.uuid4())
				filename = randname + filename
				i = Image(title=request.form['title'], filepath=filename, tags=request.form['tags'])
				db.session.add(i)
				db.session.commit()
				return jsonify(i.serialize())
	return abort(400)
'''
		if minfile:
			if min_validate():
				filedate = request.form['date']
				filename = secure_filename(infile.filename)
				randname = str(uuid.uuid4())
				filename = randname + filename
				prev_minutes = Post.query.filter_by(date=filedate).first()
				if prev_minutes:
					db.session.delete(prev_minutes)
				p = Post(date=filedate, filepath=filename)
				db.session.add(p)  
				db.session.commit()
				return jsonify(p.serialize())
		if constfile:
			filename = secure_filename(infile.filename)
			prev_const = Post.query.filter_by(date="constitution").first()
			if prev_const:
				db.session.delete(prev_const)
			c = Post(date="constitution", filepath=filename)
			db.session.add(c)
			db.session.commit()
			return jsonify(c.serialize())
'''
		#return abort(400)
	#return abort(400)


@app.route('/api/nuke/')
def nuke():
	im = Image.query.all()
	for i in im:
		db.session.delete(i)
	db.session.commit()
	return "Done."

@app.route('/api/render-post/', methods=['GET'])
def grab_posts():
	posts = list(map(lambda p: p.serialize(), Post.query.all()))
	return jsonify(posts)

@app.route('/api/render-image/', methods=['GET'])
def grab_images():
	images = list(map(lambda p: p.serialize(), Image.query.all()))
	for image in images:
		try:
			image['tags'] = image['tags'].split(",")
		except:
			pass
	return jsonify(images)


if __name__ == '__main__':
	app.run()
