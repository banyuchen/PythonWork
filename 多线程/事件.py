from multiprocessing import Event, Process
import time,random

# e = Event()     # 创建一个事件
# print(e.is_set())       #查看一个世界的状态，默认被设置成阻塞
# e.set()     # 将这个事件的状态改为Ture
# print(e.is_set())
# e.wait()    # 是根据e.is_set()的值来决定是否阻塞
# print(11111)
# e.clear()   # 将这个事件的状态改为False


# set 和 clear 分别用来修改一个事件的状态 Ture False
# is_set 用来查看一个事件的状态
# wait 依据事件的状态来决定自己的阻塞状态 False阻塞 Ture 不阻塞


def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)


def cars(e, i):
    if not e.is_set:
        e.wait()    #阻塞
        print('car % i 在等待' % i)
    print("car % i 通过" % i)


# 红绿灯事件
if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e, ))
    traffic.start()
    for i in range(20):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())

