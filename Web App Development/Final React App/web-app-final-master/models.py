from app import db


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(60))
	password = db.Column(db.String(50))
	admin = db.Column(db.Boolean, default=False)

	def serialize(self):
		return {
			'id': self.id,
			'username': self.title,
			#'password': self.password,
			'admin': self.admin,
		}

	def __repr__(self):
		return 'User'+str(self.serialize())


class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	date = db.Column(db.String(50))
	filepath = db.Column(db.String(100))

	def serialize(self):
		return {
			'id': self.id,
			'date': self.date,
			'filepath': self.filepath,
		}

	def __repr__(self):
		return 'Post'+str(self.serialize())

class Image(db.Model):
	__tablename__ = 'images'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(80))
	filepath = db.Column(db.String(100))
	tags = db.Column(db.String(500), nullable=True)
	
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'filepath': self.filepath,
			'tags': self.tags,
		}

	def __repr__(self):
		return 'Image'+str(self.serialize())
