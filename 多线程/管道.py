from multiprocessing import Pipe, Process


def func():
    pass


if __name__ == "__main__":
    conn1, conn2 = Pipe()

