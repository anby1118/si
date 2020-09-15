"""
-*- coding: utf-8 -*-
@Time    : 2020-07-27 22:01
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : user.py
"""

from .base import db
from libs.enums import MethodType
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    __tablename__ = "user_profile"
    user_profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_profile_name = db.Column(db.String(32), nullable=False)
    user_profile_email = db.Column(db.String(32), nullable=False, unique=True)
    user_profile_mobile = db.Column(db.String(11))
    # 用户的apitoken
    api_tokens = db.relationship("APIToken", backref="user_profile")
    # 定义密码
    _password = db.Column("password", db.String(128))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())

    def __str__(self):
        return f"<User {self.user_profile_name}>"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @classmethod
    def create_user(cls, user_profile_email, user_profile_name, password):
        user = cls()
        user.user_profile_name = user_profile_name
        user.user_profile_email = user_profile_email
        user.password = password
        db.session.add(user)
        db.session.commit()


api_token_permissions = db.Table("api_token_permissions",
                                 db.Column("api_token_id", db.ForeignKey("api_token.api_token_id")),
                                 db.Column("api_permission_id", db.ForeignKey("api_permission.api_permission_id")),
                                 )



class APIToken(db.Model):
    __tablename__ = "api_token"
    api_token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_token_appid = db.Column(db.String(32))
    api_token_secretkey = db.Column(db.String(32))
    user_profile_id = db.Column(db.ForeignKey('user_profile.user_profile_id'))
    permissions = db.relationship("APIPermission",
                                  secondary=api_token_permissions,
                                  backref="api_tokens")
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())



class APIPermission(db.Model):
    __talbename__ = "api_permission"
    api_permission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_permission_url = db.Column(db.String(128))
    api_permission_method_type = db.Column(db.Enum(MethodType))
    note = db.Column(db.Text)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    status = db.Column(db.Integer())
