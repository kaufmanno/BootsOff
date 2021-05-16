from bisect import bisect_left
import numpy as np


def is_sorted(a, ascending=True):
    """ Checks if a list or numpy array is sorted
    Parameters
    ----------
    a: list, numpy.array
        list or array to check

    ascending: bool
        True if sort order to check is ascending, False otherwise

    Returns
    -------
    is_sorted: bool
        returns True if a is sorted in the specified order, False otherwise
    """
    if ascending:
        return all(a[i] <= a[i + 1] for i in range(len(a) - 1))
    else:
        return all(a[i] >= a[i + 1] for i in range(len(a) - 1))


def bin_search(a, x, ascending=True, check=False):
    """ Searches where to insert a value x in an sorted list or numpy array
    Parameters
    ----------
    a: list, numpy.array
        list or array to check

    x: object
        element to insert

    ascending: bool
        True if sort order to check is ascending, False otherwise

    check: bool
        True if a has to be checked to be sorted before insertion

    Returns
    -------
    index: int
        index of the place in sorted list or array where to insert x
    """
    if check:
        if not is_sorted(a, ascending):
            print('Warning: input list is not ordered, use a=sorted(a) before calling bin_search')
            return np.nan
    if not ascending:
        print('Warning: descending sort order not implemented yet...')
        return np.nan
    else:
        #print('len(a)-1:' , len(a)-1)
        #print('max(0, bisect_left(a, x))', max(0, bisect_left(a, x)))
        return min(len(a),max(0, bisect_left(a, x)))


def insert_in_sorted(a, x, ascending=True, check=False):
    """ Searches where to insert a value x in an sorted list a and inserts it at that location
    Parameters
    ----------
    a: list, numpy.array
        list or array to check

    x: object
        element to insert

    ascending: bool
        True if sort order to check is ascending, False otherwise

    check: bool
        True if a has to be checked to be sorted before insertion

    Returns
    -------
    a: int
        sorted list with x inserted at the right position
    """

    pos = bin_search(a, x, ascending, check)

    if pos is not np.nan:
        a.insert(pos, x)

    return a
