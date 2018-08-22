import os

DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:lixn@127.0.0.1:3306/demo'