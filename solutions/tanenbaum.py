# Tanenbaum's solution

from threading import Semaphore, Thread
import time

def solution__tanenbaum():

    PHILOSOPHERS = 5

    state = ['thinking'] * PHILOSOPHERS
    sem = [Semaphore(0) for _ in range(PHILOSOPHERS)]
    mutex = Semaphore(1)

    def philosopher(i):
        print(f'starting philosopher {i}')
        time.sleep(1)

        def log(msg):
            loc = '\t\t' * i
            print(f'{loc}[P{i}]{msg}')

        def think():
            log('think')

        def eat():
            log('eat')

        def left(i): return (i + (PHILOSOPHERS - 1)) % PHILOSOPHERS
        def right(i): return (i + 1) % PHILOSOPHERS

        def get_fork(i):
            mutex.acquire()
            state[i] = 'hungry'
            test(i)
            mutex.release()
            sem[i].acquire()

        def put_fork(i):
            mutex.acquire()
            state[i] = 'thinking'
            test(right(i))
            test(left(i))
            mutex.release()

        def test(i):
            if state[i] == 'hungry' and state[left(i)] != 'eating' and state[right(i)] != 'eating':
                state[i] = 'eating'
                sem[i].release()

        while True:
            think()
            get_fork(i)
            eat()
            put_fork(i)

    [Thread(daemon=True, target=philosopher, args=(i,)).start()
     for i in range(PHILOSOPHERS)]

    input()
    exit(0)
