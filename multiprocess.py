#

import time
from multiprocessing import Process


def f(name):
    time.sleep(1)
    a = 10
    while True:
        a = a + 1
        print("hello", name, time.ctime())


if __name__ == "__main__":
    p_list = []
    for i in range(5):
        p = Process(target=f, args=('yixiang',))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
