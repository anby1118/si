"""
-*- coding: utf-8 -*-
@Time    : 2020-07-23 11:26
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : authorize.py
"""
from flask import request, current_app, g
from hashlib import md5
from models.user import APIToken
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from libs.error_code import APIAuthorizedException, AuthorizedException


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(token, password):
    """多种认证方式"""

    if token and password:
        # 如果token和password都有值表示是用户名密码认证
        return True
    elif token and token == 'api':
        # 如果token为api表示是api的请求
        return api_authorize()
    elif token:
        user_info = verify_token(token)
        g.user = user_info
        # 如果只有token有值表示是token认证
        return True
    else:
        raise APIAuthorizedException(message="参数传递不完整")

def api_authorize():
    # 获取查询参数 => get请求 => url上的参数 request.args
    # request => 当前请求（线程隔离）
    params = request.args
    appid = params.get('appid',"")
    salt = params.get('salt',"")
    sign = params.get('sign',"")

    # 获取token => 得到secretkey
    api_token = APIToken.query.filter_by(api_token_appid=appid).first()
    if not api_token:
        # => 期望json数据
        raise APIAuthorizedException(message="认证失败！没有查找到api_token")

    # 如果获取到token, 检查是否有权限
    has_permission(api_token, url=request.path, method=request.method)

    # 生成对照sign
    user_appid = api_token.api_token_appid
    user_secretkey = api_token.api_token_secretkey
    user_sign = user_appid + salt + user_secretkey
    m1 = md5()
    m1.update(user_sign.encode(encoding='utf8'))
    user_sign = m1.hexdigest()
    if sign != user_sign:
        raise APIAuthorizedException()
    else:
        return True


def has_permission(api_token, url, method):
    """权限该api是否有指定url和指定方法的权限"""
    # 从服务端查找appid及对应的秘钥
    # GET/v1/api/cmdb/servers/
    mypermission = method + url
    all_permissions = [permission.api_permission_method_type.name + permission.api_permission_url for permission in
                       api_token.permissions]
    if mypermission not in all_permissions:
        raise APIAuthorizedException(message="没有当前接口的权限")
    return True

def create_token(uid):
    s = Serializer(current_app.config["SECRET_KEY"], current_app.config["EXPIRES_IN"])

    token = s.dumps({"uid": uid}).decode(("ascii"))
    return token

def verify_token(token):
    """验证token是否合法"""
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        # 解密
        data = s.loads(token)
    except BadSignature:
        raise AuthorizedException(message='无效的Token')
    except SignatureExpired:
        raise AuthorizedException(message='Token已过期')
    return data
