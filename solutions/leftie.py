# Leftie solution

from threading import Semaphore, Thread
import time

def solution___at_least_one_leftie():

    PHILOSOPHERS = 5

    forks = [Semaphore(1) for _ in range(PHILOSOPHERS)]

    def philosopher(i: int, leftie: bool):
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

    for i in range(PHILOSOPHERS):
        if i == PHILOSOPHERS - 1:
            # at least one leftie to avoid a deadlock
            Thread(daemon=True, target=philosopher, args=(i, True)).start()
        else:
            Thread(daemon=True, target=philosopher, args=(i, False)).start()

    input()
    exit(0)
