from multiprocessing import Process, JoinableQueue
import time, random, os


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))
        q.task_done()   # 向q.join()发送一次信号，证明一个数据已经被取走了


def producer(name, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = "%s%s" % (name, i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
    q.join()    # 生产完毕，使用此方法进行阻塞，直到队列中所有项目均被处理。


if __name__ == '__main__':
    q = JoinableQueue()

    # 生产者
    p1 = Process(target=producer, args=("包子", q))
    p2 = Process(target=producer, args=("饺子", q))
    p3 = Process(target=producer, args=("馒头", q))

    # 消费者
    c1 = Process(target=consumer, args=(q, ))
    c2 = Process(target=consumer, args=(q, ))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p_l = [p1, p2, p3, c1, c2]
    [p.start() for p in p_l]

    p1.join()
    p2.join()
    p3.join()

    print("主线程执行完了")
