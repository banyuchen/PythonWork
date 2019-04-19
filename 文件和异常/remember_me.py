import json


# def get_stored_username():
#     """如果储存了名字就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def get_new_username():
#     """提示用户输入用户名"""
#     username = input("请输入您的名字")
#     filename = 'username.json'
#     with open(filename, "w") as f_obj:
#         json.dump(username, f_obj)
#         print("信息已储存")
#
#
# def greet_user():
#     """问候用户，并指出名字"""
#     username = get_stored_username()
#     if username:
#         print("欢迎回来" + username + "!")
#     else:
#         get_new_username()
#
#
# greet_user()


filename = 'register.json'


def register():
    """注册"""
    username = input("请输入用户名")
    password = input("请输入密码")
    with open(filename, 'w') as f_obj:
        content = {
            'username': username,
            'password': password,
                   }
        json.dump(content, f_obj)
        print("信息已储存")


def login():
    """登录"""
    username = input("请输入用户名")
    password = input("请输入密码")
    with open(filename, 'r') as f_obj:
        content = json.load(f_obj)
        if username == content["username"] and password == content['password']:
            print("登录成功")
        else:
            print("密码或用户名错误")

# 用户注册登录


try:
    with open(filename) as f_obj:
        login()
except FileNotFoundError:
    register()
else:
    login()
