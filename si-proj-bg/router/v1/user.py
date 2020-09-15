"""
-*- coding: utf-8 -*-
@Time    : 2020-07-24 10:24
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : user.py
"""
from flask import request, g
from libs.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource, abort
from libs.response import generate_response
from models.user import UserProfile
from serializer.user import user_schema
from libs.parse import servers_parse
from libs.handler import default_error_handler
from libs.authorize import create_token, auth
from models.user import UserProfile
from models.base import db
from forms.user import UserForm, LoginForm
from libs.error_code import FormValidateException, ArgsTypeException



user_bp = NestableBlueprint('user', __name__, url_prefix='user/')
# 定义restapi对象
api = Api(user_bp)

# 指定生产环境下，出现异常时，所调用的处理方法
# api.handle_error = default_error_handler

# @user_bp.route('/')
# def index():
#     return "this is v1/api/user/"

# 验证token
class CheckToken(Resource):
    @auth.login_required
    def get(self):
        params = request.args
        print(params)
        token = params.get("token")
        # 如果token不为Flase或false
        if token and token != "false":
            return "ok"
        else:
            return "notok"


# 定义视图
class RegisterView(Resource):
    def post(self):
        # 获取用户传过来的数据
        data = request.json

        # 验证参数有效性
        form = UserForm(data=data)
        if form.validate():
            # # 创建用户
            # user = UserProfile(user_profile_email=data.get("email"),
            #                    user_profile_name=data.get("name"),
            #                    password=data.get("password"))
            # db.session.add(user)
            # db.session.commit()
            # result = user_schema.dump(user)
            UserProfile.create_user(user_profile_email=form.email.data,
                                    user_profile_name=form.name.data,
                                    password=form.password.data)
            user = UserProfile.query.filter_by(user_profile_email=data.get("email")).first()
            result = user_schema.dump(user)

            # 返回结果
            return generate_response(data=result)
        else:
            result = form.errors
            raise FormValidateException(message=result)

class LoginView(Resource):
    def post(self):
        data = request.json
        if not data:
            raise ArgsTypeException
        # 将接收的数据绑定form，由form验证
        form = LoginForm(data=data)
        # validate函数返回了合法的用户
        user = form.validate()
        if user:
            # 生成token
            token = create_token(uid=user.user_profile_id)
            return generate_response(data={"token":token})
        else:
            result = form.errors
            raise FormValidateException(message=result)

class UserView(Resource):
    @auth.login_required
    def get(self):
        user = UserProfile.query.get(g.user["uid"])
        user_dict = user_schema.dump(user)
        return generate_response(data=user_dict)


api.add_resource(CheckToken, 'check_token/')
api.add_resource(RegisterView, 'register/')
api.add_resource(LoginView, 'login/')
api.add_resource(UserView, '/')

