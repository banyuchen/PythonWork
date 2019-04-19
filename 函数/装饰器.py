# 装饰器 函数运行前判断用户是否登录，没有登录时先登录
import json
import time


filename = 'register.json'


def register():
    """注册"""
    print("*************注册*****************")
    username = input("请输入用户名")
    password = input("请输入密码")
    with open(filename, 'w') as f_obj:
        content = {
            'username': username,
            'password': password,
            'login': False,
                   }
        json.dump(content, f_obj)
        print("信息已储存")


def login():
    """登录"""
    try:
        with open(filename, 'r') as f_obj:
            content = json.load(f_obj)
            if content['login']:
                return True
            else:
                print('*************登录*****************')
                username = input("请输入用户名")
                password = input("请输入密码")
                if username == content['username'] and password == content['password']:
                    with open(filename, 'w') as f_obj2:
                        content = {
                            'username': username,
                            'password': password,
                            'login': True,
                        }
                        json.dump(content, f_obj2)
                        print("登录成功")
                        return True
                else:
                    print("用户名或密码错误")
                    return False
    except FileNotFoundError:
        register()


def login_wrapper(func):
    """装饰器 判断是否用户是否登录"""
    def inner(*args, **kwargs):
        try:
            with open(filename):
                while True:
                    if login():
                        ret = func(*args, **kwargs)
                        return ret
        except FileNotFoundError:
            if register():
                ret = func(*args, **kwargs)
                return ret
    return inner


def log_wrapper(func):
    def inner(*args, **kwargs):
        with open("log.txt", 'a') as f_obj:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            content = "函数名:" + '"' + func.__name__ + '"             ' + "调用时间: " + now_time + "\n"
            f_obj.write(content)
            ret = func(*args, **kwargs)
        return ret
    return inner


@login_wrapper
@log_wrapper
def shoplist_add():
    print("增加一件物品")


@login_wrapper
@log_wrapper
def shoplist_del():
    print("删除一件物品")


shoplist_add()
shoplist_del()
