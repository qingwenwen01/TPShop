# 导包
import json

import app
import unittest
import requests
from api.userManagerAPI import userManager
from parameterized import parameterized

def insert_user_data():
    user_data = []
    file = app.base_path+'/data/insertUserData.json'
    with open(file, encoding='utf-8') as f:
        jsondata = json.load(f)
        for data in jsondata:
            nickname = data["nickname"]
            password = data["password"]
            mobile = data["mobile"]
            email = data["email"]
            sex = data["sex"]
            msg = data["msg"]

            user_data.append((nickname, password, mobile, email, sex, msg))
    return user_data

#新建会员管理的测试类
class TestUserManager(unittest.TestCase):
    # 前置操作--实例化接口 and 创建session对象
    def setUp(self):
        self.user_manager = userManager()
        self.session = requests.Session()
    # 后置操作--
    def tearDown(self):
        if self.session:
            self.session.close()

    # 插入会员的测试用例
    @parameterized.expand(insert_user_data())
    def test01_insert_user(self, nickname, password, mobile, email, sex, msg):
        response = self.user_manager.insert_user(session=self.session, nickname=nickname, password=password, mobile=mobile, email=email, sex=sex)
        self.assertIn(msg, response.text)