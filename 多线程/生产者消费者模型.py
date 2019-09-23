# 队列
# 生产者消费者模型
# 买包子案例

import time
import random
from multiprocessing import Process, Queue, JoinableQueue


# 生产者
def producer(name, food, q):
    for i in range(3):
        time.sleep(random.randint(1, 2))
        f = "%s生产了%s%s" % (name, food, i)
        print(f)
        q.put(f)
    q.join()    # 阻塞直到一个队列中的所有数据处理完毕 感知一个队里中的数据，是否全部被执行完毕


# 消费者
def consumer(q, name):
    while True:
        food = q.get()
        f = '\033[31m%s消费了%s\033[0m' % (name, food)
        print(f)
        time.sleep(random.randint(1, 2))
        q.task_done()


if __name__ == "__main__":
    q = JoinableQueue(20)
    p = Process(target=producer, args=("Egon", "包子", q))
    p.start()

    p1 = Process(target=producer, args=("king", "饺子", q))
    p1.start()

    c = Process(target=consumer, args=(q, "ban"))
    c.daemon = True     # 守护进程
    c.start()

    c1 = Process(target=consumer, args=(q, "jiang"))
    c1.daemon = True
    c1.start()

    p.join()
    p1.join()   # 感知一个进程的是否运行完
    # q.put(None)
    # q.put(None)

# 在消费者这段
    #   在每次获取一个数据
    #   处理一个数据
    #   发送一个记号：标记一个数据被处理

# 在生产者这一端：
    #   每一次生产一个数据
    #   且每一次生产的数据都放在队列中
    #   在队列中刻上一个记号
    #   当生产者全部生产完毕之后
    #   join信号：已经停止生产数据了
            #   且要等待之前被刻上的记号都要被消费完
            #   当数据都被处理完时，join阻塞结束


