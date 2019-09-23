'''
子进程————> 守护进程
'''
import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.5)
        print("我还活着")


if __name__ == "__main__":
    p = Process(target=func)
    p.daemon = True     # 设置子线程为守护进程
    p.start()
    i = 0
    while i < 5:
        print("我是socket server")
        time.sleep(1)
        i += 1

