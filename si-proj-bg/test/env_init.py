"""
-*- coding: utf-8 -*-
@Time    : 2020-07-24 15:03
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : env_init.py
"""
import os
import sys
basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
DB_PATH = 'sqlite:///' + os.path.join(basedir, 'test_data.sqlite')
