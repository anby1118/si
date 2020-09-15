"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 17:32
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : base.py
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from . import user