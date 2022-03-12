# 导包
import app
# 新建会员管理接口类
class userManager:
    # 初始化接口地址等信息
    def __init__(self):
        self.url_insert_user = app.base_url +'/index.php/admin/User/add_user'

    # 添加会员
    def insert_user(self, session, nickname, password, mobile, email, sex):
        insert_user_data = {
            "nickname": nickname,
            "password": password,
            "mobile": mobile,
            "email": email,
            "sex": sex
        }
        insert_user_header = {
            "Cookie": app.system_cookies
        }
        return session.post(url=self.url_insert_user, data=insert_user_data, headers=insert_user_header)
