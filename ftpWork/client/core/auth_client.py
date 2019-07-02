from core.socket_client import MySocketClient


class Auth:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """单例模式 防止多长创建socket"""
        if not cls.__instance:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self):
        self.socket = MySocketClient()
        self.username = None
        self.password = None

    def login(self):
        """登录"""
        username = input("username:").strip()
        password = input("password:").strip()
        self.username = username
        self.password = password
        if username and password:
            msg = {"username": self.username, 'password':self.password, "operation": 'login'}
            self.socket.mysend(msg)
        ret = self.socket.sk.recv(1024)# 登录结果

    def register(self):
        """注册"""
        username = input("username:").strip()
        password1 = input("password:").strip()
        password2 = input("password_ensure:").strip()
        if username and password1 and password1 == password2:
            msg = {"username": self.username, 'password':self.password, 'operation': 'register'}
            self.socket.mysend(msg)
        ret = self.socket.sk.recv(1024)# 注册结果
