# join 感知一个子进程的结束

import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*' * arg1)
    time.sleep(5)
    print('*' * arg2)


if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=func, args=(10*i, 20 *i))
        p_lst.append(p)
        p.start()
    [p.join() for p in p_lst]
    print("运行完了")