"""
@file:   test_user
@author: linuxzhen520@163.com
@date:   2020/07/24
@desc:
"""


from flask import json
import unittest
from app import create_app
from models.base import db
from env_init import DB_PATH


class TestDemo(unittest.TestCase):
    def setUp(self):
        """该方法会首先执行，相当于做测试前的准备工作，一般初始化数据使用"""
        self.app = create_app()
        # 使用flask提供的测试客户端进行测试，flask自带测试客户端，直接模拟终端请求
        self.client = self.app.test_client()
        # 开启测试模式
        self.app.debug = True
        # # 对应修改成自己测试数据库
        self.app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH

        # 先清空并创建表
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """该方法会在测试代码执行完后执行，相当于做测试后的扫尾工作"""
        # # 清除记录的测试任务
        # db.session.remove()
        # # # 清除数据库数据
        # db.drop_all()
        # self.app_context.pop()
        pass

    # 测试代码，最前面一定是test开头，才能找到函数
    def test_createuser(self):
        from libs.error_code import Success, FormValidateException
        # 预期输入 => 预期的结果 vs 实际结果是否一致
        test_data = [
            {"status_code":FormValidateException.status_code, "data":{'email': 'a@a.com'}},
            {"status_code":Success.status_code, "data":{'email': 'mm@a.com', 'password': '5623341wrwwer', 'name':'cali'}},
            {"status_code":FormValidateException.status_code, "data":{'email': 'mm@a.com', 'password': '5623341wrwwer', 'name':'cali'}},
            {"status_code":FormValidateException.status_code, "data":{'email': 'bb@a.com', 'password': '1234', 'name':'cali'}},
            {"status_code":Success.status_code, "data":{'email': 'cc@a.com', 'password': '1234abdsaf', 'name':"nono"}},
            {"status_code":Success.status_code, "data":{'email': 'dd@a.com', 'password': '1234562sdf3', 'name':'这个昵称可以'}},
        ]
        # 开始测试
        for item in test_data:
            response = self.client.post(
                '/v1/api/user/register/',
                data=json.dumps(item["data"]), content_type='application/json')
            # print(response.data.decode('utf-8'))
            ret = json.loads(response.data.decode('utf-8'))

            # print(ret.get("status_code"), ret.get("message"), ret.get("data"))
            print(item)
            print(ret)
            print(item.get("status_code"), ret.get("status_code"))
            self.assertTrue(ret.get("status_code") == item.get("status_code"))


if __name__ == '__main__':
    unittest.main()