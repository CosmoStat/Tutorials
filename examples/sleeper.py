"""Sleeper Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script makes multiple calls to the built-in sleep method to monitor
the time spent on each function call.

To run script profiling:
$ python -m cProfile sleeper.py

To run script profiling with sorted by number of calls:
$ python -m cProfile -s calls sleeper.py

"""

from time import sleep


def sleep_for_1s():
    """Sleep for 1 second
    """

    sleep(1)


def function1(n_sleeps):
    """Function 1

    Call sleep_for_1s N times.

    Parameters
    ----------
    n_sleeps: int
        Number of times to call sleep_for_1s

    """

    for _ in range(n_sleeps):
        sleep_for_1s()


def function2():
    """Function 2

    Call sleep_for_1s once.

    """

    sleep_for_1s()


def main():

    # Call function1
    function1(5)
    # Call function2
    function2()


if __name__ == '__main__':
    main()
