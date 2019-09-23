import json
import time
from multiprocessing import Process
from multiprocessing import Lock


def show(i):
    """查询余票"""
    with open('ticket') as f:
        dict = json.load(f)
    print('余票：%s' % dict['ticket'])


def buy_ticket(i, lock):
    """买票"""
    lock.acquire()
    with open('ticket') as f:
        dict = json.load(f)
        time.sleep(0.1)

    if dict['ticket'] > 0:
        dict['ticket'] -= 1
        print('%s购买成功' % i)
    else:
        print('没买到票')

    time.sleep(0.5)
    with open('ticket', 'w') as f:
        json.dump(dict, f)
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=show, args=(i, ))
        p.start()
    lock = Lock()
    for i in range(10):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()
