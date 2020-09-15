"""
-*- coding: utf-8 -*-
@Time    : 2020-07-27 22:03
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : user.py
"""
from models.user import UserProfile
from .base import ma

class UserSchema(ma.Schema):
    class Meta:
        model = UserProfile
        fields = ('user_profile_id', 'user_profile_name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)