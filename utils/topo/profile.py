# O.KAUFMANN - 2009-2020
import numpy as np
from scipy.interpolate import PPoly, PchipInterpolator
from scipy.integrate import quad
from scipy.optimize import root


def cclength(coefs, x_end=1.0):
    """ computes the length along a cubic curve defined by the coefficients of its equation z=f(x) from 0 to x_end

    :param coefs: coefficients of the cubic curve
    :type coefs: list
    :param x_end: length is computed for a portion of the curve whose ends are at x=0 and x=x_end
    :return: length the portion of the curve
    :rtype: float
    """
    # g = lambda x: (1 + (coefs[2] + 2 * coefs[1] * (x) + 3 * coefs[0] * (x) ** 2) ** 2) ** 0.5
    def g(x): return (1 + (coefs[2] + 2 * coefs[1] * x + 3 * coefs[0] * x ** 2) ** 2) ** 0.5
    length = quad(g, 0, x_end, epsrel=0.001)
    return length[0]


def cclength2abs(coefs, length):
    """ computes the x value of the point at a distance computed along a cubic curve defined by its coefficients

    :param coefs: coefficients of the cubic curve
    :type coefs: list
    :param length: length of the portion of the curve
    :type length: float
    :return: x value of the end point of the portion of the curve starting at x=0 and of given length
    :rtype: float
    """

    def f(x): return length - cclength(coefs, x)

    x = root(f, length)
    return x.x


def cclength2xz(known_points, distances):
    """ computes [x,z] of points distributed at set distances along a curve defined by a set of known points
    and interpolated as a pchip

    :param known_points: points
    :type known_points: list, numpy.array
    :param distances: distances from the origin of the curve to the points whose x_value are sought
    :type distances: numpy.array
    :return: list of found points coordinates along the curve
    :rtype: numpy.array
    """
    if type(known_points) is list:
        known_points = np.array(known_points).T
    distances = np.array(sorted(distances))
    if known_points[0][0] != 0:
        print('Error: The first known point must be at x=0.')
        return -1
    x_i = np.array(known_points[0])
    y_i = np.array(known_points[1])
    interp = PchipInterpolator(x_i, y_i)
    try:
        poly = PPoly.from_bernstein_basis(interp, extrapolate=None)
    except TypeError:
        # already a PPoly instance, nothing to do
        poly = interp
    coefs = poly.c.T
    number_of_points = len(distances)
    number_of_pieces = len(coefs)
    length_of_pieces = []
    for j in range(number_of_pieces):
        length_of_pieces.append(cclength(coefs[j], x_i[j + 1] - x_i[j]))
    i = 0
    j = 0
    xz = np.array([[np.nan, np.nan]] * number_of_points)
    while i < number_of_points:
        if distances[i] <= length_of_pieces[j]:
            xz[i, 0] = x_i[j] + cclength2abs(coefs[j], distances[i])
            xz[i, 1] = interp(xz[i, 0])
            i += 1
        elif j < number_of_pieces - 1:
            distances = distances - length_of_pieces[j]
            j += 1
        else:
            for k in range(i, number_of_points):
                xz[k, 0] = np.nan
                xz[k, 1] = np.nan
            break
    return xz


def cclengths(known_points):
    """ computes the distance from the first point and each given point along a curve defined
    by this set of known points and interpolated as a pchip

    :param known_points: points
    :type known_points: list, numpy.array
    :return: list of distances along the curve
    :rtype: numpy.array
    """
    if type(known_points) is list:
        known_points = np.array(known_points).T
    if known_points[0][0] != 0:
        print('Error: The first known point must be at x=0.')
        return -1
    x_i = np.array(known_points[0])
    y_i = np.array(known_points[1])
    interp = PchipInterpolator(x_i, y_i)
    try:
        poly = PPoly.from_bernstein_basis(interp, extrapolate=None)
    except TypeError:
        # already a PPoly instance, nothing to do
        poly = interp
    coefs = poly.c.T
    number_of_pieces = len(coefs)
    length_of_pieces = []
    for j in range(number_of_pieces):
        length_of_pieces.append(cclength(coefs[j], x_i[j + 1] - x_i[j]))
    return np.hstack([np.array([0]), np.cumsum(np.array(length_of_pieces))])


if __name__ == '__main__':
    known_points = [[0, 284], [58, 280], [152, 275], [217, 270], [228, 267], [305, 265], [340, 260], [374, 255],
                    [397, 250], [417, 245], [459, 240], [484, 245], [539, 250], [687, 245]]
    xz = cclength2xz(known_points, np.linspace(0, 800, 81))
    print(xz)
