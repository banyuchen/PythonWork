import socketserver
import json
from server.core import views


class MyFTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = self.my_recv()
        # 消息的转发 把任务转给view文件中的对应的方法
        op_str = msg['operation']
        if hasattr(views, op_str):
            func = getattr(views, op_str)
            func(msg)

    def my_recv(self):
        msg = self.request.recv(1024)
        msg = msg.decode("utf-8")
        msg = json.loads(msg)
        return msg