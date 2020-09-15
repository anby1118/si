"""
-*- coding: utf-8 -*-
@Time    : 2020-07-17 15:05
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : __init__.py
"""

from .base import ma

def init_app(app):
    ma.__init__(app)