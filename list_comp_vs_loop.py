"""List Comprehension vs Loop Example

:Author: Samuel Farrens <samuel.farrens@cea.fr>

This script demonstrates how list comprehension in Python is more efficient
than a basic loop for creating list objects.

To run with profiling:
$ python -m cProfile list_comp_vs_loop.py

"""


def cubes_loop(n):
    """List of Cubes

    Function to calculate the cube of numbers in a range from zero to n.

    Parameters
    ----------
    n : int
        Number of cubes to store in list

    Returns
    -------
    list
        List of cubes

    Notes
    -----
    This function implments a slower loop.

    """

    new_list = []

    for i in range(n):
        new_list.append(n ** 3)

    return new_list


def cubes_list_comp(n):
    """List of Cubes

    Function to calculate the cube of numbers in a range from zero to n.

    Parameters
    ----------
    n : int
        Number of cubes to store in list

    Returns
    -------
    list
        List of cubes

    Notes
    -----
    This function implments a faster list comprehension.

    """

    return [x ** 3 for x in range(n)]


def main():

    n_cubes = int(1e7)

    res_loop = cubes_loop(n_cubes)
    res_list_comp = cubes_list_comp(n_cubes)


if __name__ == '__main__':
    main()
