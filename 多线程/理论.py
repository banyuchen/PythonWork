# 多进程
from multiprocessing import Process
import os,time


def func(dict):
    print(dict)
    print("子进程：", os.getpid())


p = Process(target=func, args=("参数", ))    # 注册一个子进程
# p 是一个进程对象
p.start() # 启动一个进程
print("主线程：", os.getpid())