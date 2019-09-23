import time
from multiprocessing import Pool


def func(i):
    time.sleep(0.5)
    return i*i


if __name__ == "__main__":
    p = Pool(5)
    for i in range(10):
        res = p.apply_async(func, args=(i, ))
        print(res)

