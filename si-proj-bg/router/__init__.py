"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 16:02
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : __init__.py
"""

from .v1 import v1_bp

def init_app(app):
    app.register_blueprint(v1_bp)