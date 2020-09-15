"""
-*- coding: utf-8 -*-
@Time    : 2020-07-24 10:17
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : user.py
"""

from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError
from models.user import UserProfile
from werkzeug.security import check_password_hash
from libs.error_code import AuthorizedException


class UserForm(Form):
    email = StringField(validators=[DataRequired(), Email(message="邮箱不合法")])
    password = StringField(validators=[DataRequired(), Regexp(r'^\w{6,18}$', message="密码复杂度不符合要求")])
    name = StringField(validators=[DataRequired()])

    def validate_email(self, value):
        # 验证email是否在数据库已经存在
        print("check_email")
        if UserProfile.query.filter_by(user_profile_email=value.data).first():
            raise ValidationError("邮箱已存在！")

    # 用户名长度6~16位之间
    def validate_name(self, value):
        print("check_name")

    # # 整体验证
    def validata(self):
        print("整体验证")
        return super().validate()

class LoginForm(Form):
    # 这里用这个名字接收数据是由于前端iview-admin使用的是这个名字，在那边修改成本比较大，因此改这边
    email = StringField(validators=[DataRequired(), Email(message="邮箱不合法")])
    password = PasswordField(validators=[DataRequired()])

    def validate(self):
        # 验证用户名密码
        super().validate()
        # user = UserProfile.query.filter_by(user_profile_email=self.userName.data).first()
        # if user and check_password_hash(user.password, self.password.data):
        #     return user
        # else:
        #     raise AuthorizedException(message="用户名或密码错误")

        if self.errors:
            return False
        user = UserProfile.query.filter_by(user_profile_email=self.email.data).first()
        if user and check_password_hash(user.password, self.password.data):
            return user
        else:
            raise AuthorizedException(message="用户名或密码错误")


