# 封装被测试系统的登陆接口

# 导包
import app
# 定义登陆接口类
class loginAPI:

    # 初始化接口地址
    def __init__(self):
        self.url_verify = app.base_url + "/index.php?m=Home&c=User&a=verify"
        self.url_login = app.base_url + "/index.php?m=Home&c=User&a=do_login"

    # 获取验证码
    def get_verify_code(self, session):
        return session.get(url=self.url_verify)

    # 发送登陆请求
    def login(self, session, username, password, verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        return session.post(url=self.url_login, data=login_data)