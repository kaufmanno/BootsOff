from bisect import bisect_left
import numpy as np


def check_order(a):
    """ Check if a list is ordered
    :param a: ordered list
    :type a: list
    :return: True if a is ordered, False otherwise
    :rtype: bool
    """

    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def bin_search(a, x, check=False):
    """ searches where to insert a value x in an ordered list a
    :param a: ordered list
    :type a: list
    :param x: value to insert
    :type x: int or float
    :param check: check whether a is ordered or not
    :type check: bool
    :return: index in ordered list where to insert x
    :rtype: int
    """
    if check:
        if not check_order(a):
            print('Warning: input list is not ordered, use a=sorted(a) before calling bin_search')
            return np.nan

    print('len(a)-1:' , len(a)-1)
    print('max(0, bisect_left(a, x))', max(0, bisect_left(a, x)))
    return min(len(a),max(0, bisect_left(a, x)))


def insert_in_order(a, x, check=False):
    """ searches where to insert a value x in an ordered list and insert it at that location
    :param a: ordered list
    :type a: list
    :param x: value to insert
    :type x: int or float
    :param check: check whether a is ordered or not
    :type check: bool
    :return: ordered list with x inserted at the right position
    :rtype: list
    """

    pos = bin_search(a, x, check)

    if pos is not np.nan:
        a.insert(pos, x)

    return a


if __name__ == '__main__':
    a = [3., 7., 11.5, 99.1]
    x = 11.9

    print('list before insertion: ', a)
    insert_in_order(a, x, True)
    print('list after insertion: ', a)