# Dining Philosophers Problem
[This repository](https://github.com/debemdeboas/dpp) contains solutions for the [Dining Philosophers Problem (DPP)](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

## Solutions

Each solution is self-contained in its own file in the `solutions/` directory.

### "Leftie" solution

This solution consists of having at least one leftie and one rightie philosopher.
The leftie will prioritize getting its `left(i)` fork first, and the rightie will try to pick its `right(i)` fork first.

This solution is guaranteed to work with no deadlocks indefinetely.

### Tanenbaum's solution

This solution consists of giving each philosopher one of three states (thinking, hungry or eating).

```python
PHILOSOPHERS = 5
state = ['thinking'] * PHILOSOPHERS
sem = [Semaphore(0) for _ in range(PHILOSOPHERS)]
mutex = Semaphore(1)
```

- `sem` indicates whether a philosopher can start eating or not.
- `mutex` is used so that no two philosophers may access the pickup or putdown list at the same time.
- The `state` list is used to know the state of each philosopher.

A philosopher will only eat if its neighbors are not eating.

This solution is more difficult to understand and can result in a starvation situation, as stated by [Allen Downey in *The Little Book of Semaphores*](https://weinman.cs.grinnell.edu/courses/CSC213/2012F/labs/philosophers.html).

## Running the program

Running the program is straightforwad, as always:

```commandline
python main.py
```

The user is greeted by a menu with an option each corresponding to a different solution.
The user shall enter their desired solution and that's it.
To stop the execution, input any key at any time and the threads will be `join()`ed.
