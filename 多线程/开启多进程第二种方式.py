import os
from multiprocessing import Process
'''
自定义类 继承Process类
必须实现一个run方法，run方法中是在子线程中执行的代码
'''


class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(os.getpid())
        print(self.arg1)
        print(self.arg2)


if __name__ == "__main__":
    print("主线程：", os.getpid())
    p1 = MyProcess(1, 2)
    p1.start()
    p2 = MyProcess(3, 4)
    p2.start()

