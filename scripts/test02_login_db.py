'''
定义接口测试用例，使用unittest
步骤：1、导包
2、创建测试类
  2.1、前置处理
  2.2、后置处理
  2.3、创建测试方法
'''

# 导包
import app
import requests
import unittest
from api.login import loginAPI
from parameterized import parameterized
from tools.dbutil import  DBUtil

# 从数据库中导入测试数据
def login_data():
    logindata = []
    sql = 'select * from t_login'
    db_data = DBUtil.exe_sql(sql)
    print(db_data)
    for data in db_data:
        username = data[2]
        password = data[3]
        verify_code = data[4]
        verify_status_code = data[5]
        status = data[7]
        msg = data[8]
        logindata.append((username, password, verify_code, verify_status_code, status, msg))

    return logindata

# 创建测试类
class TestLogin01(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = loginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建session对象
    # 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    # 创建测试用例
    def test01_verify_code_error(self):
        # 获取验证码
        response1 = self.login_api.get_verify_code(self.session)
        print(response1.status_code)
        print(response1.headers.get("Content-Type"))
        self.assertEqual(200, response1.status_code)
        self.assertIn('image', response1.headers.get("Content-Type"))
        # 登陆
        response = self.login_api.login(session=self.session, username='12345678900', password='1', verify_code='8888')
        print(response.status_code)
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json().get("status"))
        self.assertIn('验证码错误', response.json().get("msg"))

    # 参数化
    @parameterized.expand(login_data())
    def test02_login_succes(self,username, password, verify_code, verify_status_code, status, msg):
        # 获取验证码
        response1 = self.login_api.get_verify_code(self.session)
        print(response1.status_code)
        print(response1.headers.get("Content-Type"))
        self.assertEqual(verify_status_code, response1.status_code)
        self.assertIn('image', response1.headers.get("Content-Type"))
        # 登陆
        response = self.login_api.login(session=self.session, username=username, password=password, verify_code=verify_code)
        print(response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))

    def test03_password_error(self):
        pass