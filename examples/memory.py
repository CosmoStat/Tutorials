"""Memory Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script demonstrates how to track the memory allocated and freed from
objects.

To run inline profiling:
$ python -m memory_profiler memory.py

To run script profiling:
$ mprof run memory.py
$ mprof plot

"""


from time import sleep


@profile
def memory_eater():
    """Memory Eater

    This function creates a list and increases the memory consumption several
    times before deleting the object.

    """

    big_list = [2]
    sleep(1)

    big_list *= (10 ** 7)
    sleep(1)

    big_list *= 2
    sleep(1)

    big_list *= 2
    sleep(1)

    del big_list


def main():

    memory_eater()


if __name__ == '__main__':
    main()
