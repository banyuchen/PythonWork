from core.auth_client import Auth


def main():
    """选择执行菜单"""
    auth_obj = None
    start_1 = [("登录", 'login'), ('注册', 'register'), ('退出','exit')]
    for index, item in enumerate(start_1):
        print(index, item[0])

    while True:
        try:
            num = int(input(">>>"))
            func_str = start_1[num-1][1]


        except:
            print("您输入的信息有误")

        if hasattr(Auth, func_str):
            auth_obj = Auth()
            func = getattr(auth_obj, func_str)
            ret = func()
            if ret:
                break
        elif auth_obj:
            auth_obj.sk.close()
            exit()
        else:
            exit()