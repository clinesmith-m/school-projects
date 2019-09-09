import datetime
from app import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    profilepic = db.Column(db.String(100))
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, firstname, lastname, username, password, email, profilepic):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.profilepic = profilepic

    def __repr__(self):
        return 'user(uid={}, firstname={}, lastname={}, username{}, password{}, email={}, dateofreg={})'.format(self.uid, self.firstname,\
self.lastname, self.username, self.password, self.email, self.dateofreg)


class Post(db.Model):
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000), nullable=True)
    imgpath = db.Column(db.String(100), nullable=True)
    puid = db.Column(db.Integer)#, db.ForeignKey('user.uid'))

    def __init__(self, title, description, imgpath, puid):
        self.title = title
        self.description = description
        self.imgpath = imgpath
        self.puid = puid

    def __repr__(self):
        return 'post(pid={}, title={}, description={}, imgpath={}, puid={}'.format(self.pid, self.title, self.description, self.imgpath, self.puid)

db.create_all()
