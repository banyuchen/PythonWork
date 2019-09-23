from multiprocessing import Process
import time
import random


def ktv(i):
    print("%s走进ktv" % i)
    time.sleep(random.randint(1, 5))
    print("%s走出ktv" % i)


if __name__ == "__main__":
    for i in range(20):
        p = Process(target=ktv, args=(i,))
        p.start()