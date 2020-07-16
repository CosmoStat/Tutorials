"""Efficient vs Inefficient Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script demonstrates how certain calculations can be implemented more
efficiently to reduce computation time.

To run with profiling:
$ python -m cProfile efficient.py

"""


import math


def calculate_inefficient(val_range):
    """Calculate Inefficiently

    Take a range of input values and perform some calculations on each entry.

    Parameters
    ----------
    val_range : list
        List of values

    Returns
    -------
    list
        List of results

    Notes
    -----
    For the inefficient approach we recalculate the square root of 1001 twice
    for every input value. We also store the square of every computation.

    """

    res = []

    for val in val_range:

        res.append((math.sin(val) * math.sqrt(1001),
                    (math.sin(val) * math.sqrt(1001)) ** 2))

    return res


def top_vals_inefficient(values, n):
    """Top 5 Inefficient Values

    Take the first 5 value pairs from the list.

    Parameters
    ----------
    values : list
        Values obtained from calculate_inefficient
    n : int
        Number of values to return

    Returns
    -------
    list
        First five entries in the list

    """

    return values[:n]


def calculate_efficient(val_range):
    """Calculate Efficiently

    Take a range of input values and perform some calculations on each entry.

    Parameters
    ----------
    val_range : list
        List of values

    Returns
    -------
    list
        List of results

    Notes
    -----
    For the efficient approach we pre-compute the square root of 1001.

    """

    res = []
    sqrt_val = math.sqrt(1001)

    for val in val_range:

        res.append(math.sin(val) * sqrt_val)

    return res


def top_vals_efficient(values, n):
    """Top 5 Efficient Values

    Take the first 5 values and calculate the corresponding squares.

    Parameters
    ----------
    values : list
        Values obtained from calculate_efficient
    n : int
        Number of values to return

    Returns
    -------
    list
        First five value pairs

    """

    return [(val, val ** 2) for val in values[:n]]


def main():

    n_values = int(1e7)
    val_range = [i * (1. / n_values) for i in range(n_values)]

    res_ineff = calculate_inefficient(val_range)
    t5_ineff = top_vals_inefficient(res_ineff, 5)

    res_eff = calculate_efficient(val_range)
    t5_eff = top_vals_efficient(res_eff, 5)


if __name__ == '__main__':
    main()
