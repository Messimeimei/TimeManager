# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2023/3/29 19:05

""""""
from flask import Flask

def register_bp(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from .app_login import login as login_blueprint
    app.register_blueprint(login_blueprint)


def create_app():
    app = Flask(__name__)
    with app.app_context():
        register_bp(app)
    return app