# coding:   utf-8
# 作者(@Author):   Messimeimei
# 创建时间(@Created_time): 2023/3/29 20:34

"""登录视图函数"""
from . import login
from flask import render_template


@login.route('/', methods=['GET', 'POST'])
def a():
    return render_template("register.html")
