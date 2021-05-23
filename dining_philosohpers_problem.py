# Leftie solution
def solution___at_least_one_leftie():
    from threading import Semaphore, Thread
    import time

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


# Tanenbaum's solution
def solution__tanenbaum():
    from threading import Semaphore, Thread
    import time

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

    [Thread(daemon=True, target=philosopher, args=(i,)).start() for i in range(PHILOSOPHERS)]

    input()
    exit(0)


print('* DPP SOLUTIONS *')
print('To stop execution, press Ctrl + C at any time\n')
print('--- Choose your solution type ---')
print('\t1: Leftie solution')
print('\t2: Tanenbaum solution')
if (choice := input('> ')).isdigit():
    if choice == '1':
        solution___at_least_one_leftie()
    elif choice == '2':
        solution__tanenbaum()
    else:
        print('Invalid choice :(')
        exit(1)
else:
    print('Please only input numbers')
    exit(2)
