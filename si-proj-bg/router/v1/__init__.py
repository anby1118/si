"""
-*- coding: utf-8 -*-
@Time    : 2020-07-18 17:18
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : __init__.py
"""

from libs.nestable_blueprint import NestableBlueprint
from .user import user_bp

v1_bp = NestableBlueprint('v1', __name__, url_prefix='/v1/api/')
v1_bp.register_blueprint(user_bp)