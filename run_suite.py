# 导包
import time
import app
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test01_login import TestLogin
from scripts.test02_login_db import TestLogin01
from scripts.test03_insert_user import TestUserManager
import unittest
# 封装测试套件
suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestLogin01))
suite.addTest(unittest.makeSuite(TestUserManager))
# 指定测试报告路径
report = app.base_path+'/report/report-{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
# 文件流形式打开文件
with open(report, "wb") as f:
    #创建HTMLTestRunner的运行器
    runner = HTMLTestRunner(f, title="tpshop添加会员接口测试")
    # 执行测试套件
    runner.run(suite)