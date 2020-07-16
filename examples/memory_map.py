"""Memory Map Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script demonstrates how memory mapping reduces the memory consumption for
numpy objects.

To run inline profiling:
$ python -m memory_profiler memory_map.py

To run script profiling:
$ mprof run memory_map.py
$ mprof plot

"""


import numpy as np
from time import sleep


@profile
def create_data(file_name):
    """Create Data

    Create example data and save to a file.

    Parameters
    ----------
    file_name : str
        Example data file name

    """

    data = [2] * (2 * 10 ** 7)
    np.save(file_name, np.array(data))

    del data


@profile
def read_data(file_name):
    """Read Data

    Read data from a file.

    Parameters
    ----------
    file_name : str
        Example data file name

    """

    data = np.load(file_name)
    sleep(1)

    del data
    sleep(1)


@profile
def map_data(file_name):
    """Map Data

    Read data from a file using mempory mapping.

    Parameters
    ----------
    file_name : str
        Example data file name

    """

    data = np.load(file_name, mmap_mode='r')
    sleep(1)

    del data
    sleep(1)


def main():

    file_name = 'example_data.npy'

    create_data(file_name)
    read_data(file_name)
    map_data(file_name)


if __name__ == '__main__':
    main()
