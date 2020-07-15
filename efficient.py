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


def top_five_inefficient(values):
    """Top 5 Inefficient Values

    Take the first 5 value pairs from the list.

    Parameters
    ----------
    values : list
        Values obtained from calculate_inefficient

    Returns
    -------
    list
        First five entries in the list

    """

    return values[:5]


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


def top_five_efficient(values):
    """Top 5 Efficient Values

    Take the first 5 values and calculate the corresponding squares.

    Parameters
    ----------
    values : list
        Values obtained from calculate_efficient

    Returns
    -------
    list
        First five value pairs

    """

    return [(val, val ** 2) for val in values[:5]]


def main():

    n_values = int(1e7)
    val_range = [i * (1. / n_values) for i in range(n_values)]

    res_ineff = calculate_inefficient(val_range)
    t5_ineff = top_five_inefficient(res_ineff)

    res_eff = calculate_efficient(val_range)
    t5_eff = top_five_efficient(res_eff)


if __name__ == '__main__':
    main()
