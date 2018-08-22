from flask import Flask,render_template,request,redirect,url_for,session
from exts import db
from models import User,Questions
import config
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter(User.username == username,User.password == password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for("index"))
        else:
            return "用户名或者密码错误，请确认！"

@app.route('/registe/',methods=['GET','POST'])
def registe():
    if request.method == 'GET':
        return render_template('registe.html')
    else:
        username = request.form.get('username')
        password1= request.form.get('password1')
        password2= request.form.get('password2')
        user = User.query.filter(User.username==username).first()
        if not user:
            if password1 == password2:
                user = User(username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login"))
        else:
            return "用户名已存在,请重新输入"

@app.route("/logout/")
def logout():
    session.pop('user_id',None)
    return redirect(url_for("login"))

@app.route("/post/")
def post():
    if request.method == 'GET':
        return render_template("post.html")
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = session.get('user_id')
        author = User.query.filter(id=user_id)
        question = Questions(title=title,content=content,author=author)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("index"))

@app.before_request
def beore_request():
    """全局变量g只在请求当中有效"""
    pass
@app.context_processor
def context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id)
        return {'username':user.username}
    else:
        return dict()

if __name__ == '__main__':
    app.run()
