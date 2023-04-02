# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2023/3/29 20:34

"""登录视图"""
from flask import Blueprint

login = Blueprint("login", __name__)
from . import view
