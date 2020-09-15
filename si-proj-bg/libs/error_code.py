"""
@file:   error_code
@author: linuxzhen520@163.com
@date:   2020/07/22
@desc:
"""

from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    # code: http返回码
    code = 500
    # message: 默认情况下，出了异常message信息
    message = "opps!"
    # status_code: 默认情况下，业务状态码
    status_code = 9999

    def __init__(self, message=None, code=None, status_code=None, headers=None):
        if code:
            self.code = code
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message
        # super().__init__(description=msg)
        super().__init__(message, None)

    def get_body(self, environ=None):
        """返回的数据内容，可看父类源码"""
        import json
        body = dict(
            message=self.message,
            status_code=self.status_code
        )
        content = json.dumps(body)
        return content

    def get_headers(self, environ=None):
        """返回json格式数据，可看父类源码"""
        return [('Content-Type', 'application/json')]

class APIAuthorizedException(APIException):
    message = "用户认证失败"
    status_code = 10004

class FormValidateException(APIException):
    """自定义异常类测试"""
    message = "表单验证失败"
    status_code = 10002

class Success(object):
    message = "OK"
    status_code = 10000

class ArgsTypeException(APIException):
    message = "请求方式错误"
    status_code = 10003

class AuthorizedException(APIException):
    message = "用户认证失败"
    status_code = 10001
    code = 401
