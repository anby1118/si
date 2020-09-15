"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 15:17
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : app.py
"""


import os
from flask_cors import CORS
from flask import Flask

def create_app(config=None):
    # 创建app
    # 实例化一个app
    # Flask("字符串")
    # 字符串用来Flask对象标识，通常用__name__
    # Flask函数可以接收功能多参数，来配置静态模板中js/css/png等的解析方法
    app = Flask(__name__)
    CORS(app, resources={'*': {'origins': '*'}})

    # load default configuration
    # 加载配置: config.settings和config.secure是模块路径
    app.config.from_object('config.settings')
    app.config.from_object('config.secure')
    # load environment configuration
    # FLASK_CONF="/path/to/config_dev.py"
    # FLASK_CONF="/path/to/config_prod.py"
    # 也可以根据系统环境变量，加载不同的配置文件
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    # 注册蓝图
    import router, models, serializer
    router.init_app(app)

    # 将model注册到app
    models.init_app(app)

    # 将序列化器注册到app
    serializer.init_app(app)
    # 返回核心对象
    return app