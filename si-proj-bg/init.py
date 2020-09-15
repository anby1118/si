"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 11:31
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : init.py
"""

# 导入flask核心对象
from app import create_app
app = create_app()

if __name__ =='__main__':
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG']
    )