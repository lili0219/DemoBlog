from exts import db

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


