"""
-*- coding: utf-8 -*-
@Time    : 2020-07-22 10:26
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : response.py
"""
from libs.error_code import Success

def generate_response(data=None, message=Success.message, status_code=Success.status_code):
    if data is None:
        data = []

    return {
        "message": message,
        "status_code": status_code,
        "data": data
    }