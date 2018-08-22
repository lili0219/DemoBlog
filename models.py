from exts import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def __init__(self,username,password):
        self.username = username
        self.password = password

class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(128))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('User',backref="questions")
    createtime = db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self,title,content,author_id):
        self.title     = title
        self.content   = content
        self.author_id = author_id

class Reply(db.Model):
    __tablename__ = "replys"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.String(128))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', backref="replys")
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('Questions', backref=db.backref('replys',order_by = id.desc()))
    createtime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self,content,author_id,question_id):
        self.content = content
        self.author_id = author_id
        self.question_id = question_id
