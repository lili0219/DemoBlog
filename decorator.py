from functools import wraps
from flask import session

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        #return func(*args,**kwargs)
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return
    return wrapper
"""
带参数的装饰器
"""
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args,**kwargs):
            print("[{level}]:enter function {func}()".format(level=level,
                                                             func=func.__name__))
            return func(*args,**kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

if __name__ == '__main__':
    say('Hello')