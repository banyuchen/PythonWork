'''
进程与进程之间
'''
import os
from multiprocessing import Process


def func():
    global n
    n = 0
    print('pid:', os.getpid(), n)


if __name__ == "__main__":
    n = 100
    p = Process(target=func)
    p.start()
    p.join()
    print("主线程：", os.getpid(), n)

