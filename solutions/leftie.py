# Leftie solution

from threading import Semaphore, Thread
import time
from typing import Callable


def solution___at_least_one_leftie():

    PHILOSOPHERS = 5

    forks = [Semaphore(1) for _ in range(PHILOSOPHERS)]

    def philosopher(i: int, leftie: bool, stop: Callable):
        print(f'starting philosopher {i} | leftie? {leftie}')
        time.sleep(1)

        def log(msg):
            loc = '\t\t' * i
            print(f'{loc}[P{i} L:{str(leftie)[:1]}]{msg}')

        def think():
            log('think')

        def eat():
            log('eat')

        def get_left(i): return i
        def get_right(i): return (i + 1) % PHILOSOPHERS

        def get_forks(i):
            if leftie:
                forks[get_left(i)].acquire()
                forks[get_right(i)].acquire()
            else:
                forks[get_right(i)].acquire()
                forks[get_left(i)].acquire()

        def put_forks(i):
            forks[get_right(i)].release()
            forks[get_left(i)].release()

        while True:
            think()
            get_forks(i)
            eat()
            put_forks(i)

            if stop():
                log('stopping')
                break

    stop_threads = False
    workers = []
    for i in range(PHILOSOPHERS):
        if i == PHILOSOPHERS - 1:
            # at least one leftie to avoid a deadlock
            thr = Thread(daemon=True, target=philosopher, args=(i, True, lambda: stop_threads))
        else:
            thr = Thread(daemon=True, target=philosopher, args=(i, False, lambda: stop_threads))
        workers.append(thr)
        thr.start()

    input()
    stop_threads = True
    [thr.join() for thr in workers]
    exit(0)
