"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 17:37
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : __init__.py
"""

from .base import db

def init_app(app):
    db.init_app(app)
    # 程序中使用命令创建数据库
    db.create_all(app=app)
