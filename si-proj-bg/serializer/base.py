"""
-*- coding: utf-8 -*-
@Time    : 2020-07-17 15:00
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : base.py
"""
from flask_marshmallow import Marshmallow
ma = Marshmallow()

# 把定义的序列化内容加载到ma
from . import user