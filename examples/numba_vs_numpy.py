"""Numba vs Numpy Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script demonstrates how Numba can help speed up certain Numpy
implementations, in particular where multiple call as made to the same
funciton.

To run with profiling:
$ python -m cProfile numba_vs_numpy.py

"""

import numpy as np
from numba import jit


def trace_numpy(a):
    """Trace Numpy

    Calculate tanh of diagonal elements of input matrix.

    Parameters
    ----------
    a : numpy.ndarray
        2D matrix

    """

    trace = 0.0

    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])


@jit(nopython=True)
def trace_numba(a):
    """Trace Numba

    Calculate tanh of diagonal elements of input matrix.

    Parameters
    ----------
    a : numpy.ndarray
        2D matrix

    Notes
    -----
    Use Numba jit speed up

    """
    trace = 0.0

    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])


def function_numpy(a, n):
    """Function Numpy

    Call trace_numpy n times.

    Parameters
    ----------
    a : numpy.ndarray
        2D matrix
    n : int
        Number of times to call trace_numpy

    """

    for _ in range(n):
        trace_numpy(a)


def function_numba(a, n):
    """Function Numba

    Call trace_numba n times.

    Parameters
    ----------
    a : numpy.ndarray
        2D matrix
    n : int
        Number of times to call trace_numba

    """

    for _ in range(n):
        trace_numba(a)


def main():

    a = np.arange(int(1e6)).reshape(1000, 1000)
    n_calls = 1000

    function_numpy(a, n_calls)
    function_numba(a, n_calls)


if __name__ == '__main__':
    main()
