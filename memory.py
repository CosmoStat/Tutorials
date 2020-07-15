"""Memory Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>



To run:
$ python -m memory_profiler memory.py

"""


from time import sleep
from random import randint


@profile
def memory_eater():

    bignum_list = []
    bignum_range = (1e30, 1e31)

    for _ in range(int(1e6)):

        bignum_list.append(randint(*bignum_range))


def main():

    memory_eater()


if __name__ == '__main__':
    main()
