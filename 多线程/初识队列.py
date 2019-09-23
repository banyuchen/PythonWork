from multiprocessing import Queue,Process


def produce(q):
    q.put("Hello")


def consume(q):
    print(q.get())


if __name__ == "__main__":
    q = Queue()

    p = Process(target=produce, args=(q,))
    p.start()

    p2 = Process(target=consume, args=(q,))
    p2.start()
