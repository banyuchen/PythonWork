import time
import random
from multiprocessing import Process, Semaphore


def ktv(i, lock):
    lock.acquire()
    print('%s走进ktv' % i)
    time.sleep(random.randint(1, 5))
    print('%s走出ktv' % i)
    lock.release()


lock = Semaphore(4)
for i in range(20):
    p = Process(target=ktv, args=(i, lock))
    p.start()



