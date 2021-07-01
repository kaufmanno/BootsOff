import matplotlib.pyplot as plt
import pyvista as pv
import numpy as np
from shapely.geometry import Point, LineString, LinearRing, Polygon
from descartes import PolygonPatch


def plot_shapely_obj(ax=None, obj=None, **kwargs):
    """
    Plots a shapely object in matplotlib axes
    Parameters
    ----------
    ax : matplotlib.axes
        axes in which the shapely object should be plotted
    obj : shapely.geometry
        a shapely object to plot
    kwargs : dict
        keywords and arguments to pass to matplotlib plot for Points, LineStrings or LinearStrings and to patches for
        polygons

    Returns
    -------
       the matplotlib axes object used to plot the shapely object
    """
    if ax is None:
        fig, ax = plt.subplots()
    if isinstance(obj, Point) or isinstance(obj, LineString) or isinstance(obj, LinearRing):
        x, y = obj.xy
        ax.plot(x, y, **kwargs)
    elif isinstance(obj, Polygon):
        patch = PolygonPatch(obj, **kwargs)
        ax.add_patch(patch)
    else:
        print(f'Warning: Invalid object type - {obj} : {type(obj)}')
    return ax


def transform_matrix_2d(from_obj, to_obj, shapely_format=False):
    # TODO: deal with more than two points in from_points and to_points using best fit ?
    # TODO: introduce skew?
    if type(from_obj) is not tuple:
        f = (*from_obj.coords[0], *from_obj.coords[-1])
        f_length = from_obj.length
    else:
        f = from_obj
        f_length = np.sqrt((f[2] - f[0]) ** 2 + (f[3] - f[1]) ** 2)
    if type(to_obj) is not tuple:
        t = (*to_obj.coords[0], *to_obj.coords[-1])
        t_length = to_obj.length
    else:
        t = to_obj
        t_length = np.sqrt((t[2] - t[0]) ** 2 + (t[3] - t[1]) ** 2)
    print(f, t)
    theta = np.arctan2(t[3] - t[1], t[2] - t[0]) - np.arctan2(f[3] - f[1], f[2] - f[0])
    ct = np.cos(theta)
    st = np.sin(theta)
    sf = (t_length / f_length)
    t1x = -f[0]
    t1y = -f[1]
    t2x = t[0]
    t2y = t[1]

    a = sf * ct
    b = -sf * st
    c = 0.
    # noinspection SpellCheckingInspection
    xoff = t1x * sf * ct - t1y * sf * st + t2x
    d = sf * st
    e = sf * ct
    f = 0.
    # noinspection SpellCheckingInspection
    yoff = t1x * sf * st + t1y * sf * ct + t2y
    g = 0.
    h = 0.
    i = 1.
    # noinspection SpellCheckingInspection
    zoff = 0.

    if shapely_format:
        return [a, b, c, d, e, f, g, h, i, xoff, yoff, zoff]
    else:
        return np.array([[a, b, c, xoff], [d, e, f, yoff], [g, h, i, zoff], [0., 0., 0., 1.]])


def plot_profile(ax=None, obj=None, name=''):
    if type(obj) is LineString:
        ax = plot_shapely_obj(ax=ax, obj=obj, color='k', linestyle='--', linewidth=0.75)
        plot_shapely_obj(ax=ax, obj=Point(obj.coords[0]), marker='o', color='g')  # start
        for i in range(1, len(obj.coords)):
            plot_shapely_obj(ax=ax, obj=Point(obj.coords[i]), marker='x', color='grey')
        plot_shapely_obj(ax=ax, obj=Point(obj.coords[-1]), marker='s', color='r')  # end
        theta = np.arctan2(obj.coords[-1][1] - obj.coords[0][1], obj.coords[-1][0] - obj.coords[0][0]) * 180. / np.pi
        ax.text(obj.centroid.coords[0][0], obj.centroid.coords[0][1], name, rotation=theta,
                horizontalalignment='center', verticalalignment='top', multialignment='center')
        ax.axis('equal')
    return ax


def transform_vtk(transform_matrix, infile, outfile=None):
    """ transforms a vtk file using an affine transform in 3D defined by the transform matrix
    :param transform_matrix: a 4x4 affine transform matrix
    :param infile: filename of a vtk file to transform
    :param outfile: filename of the transformed vtk file"""

    # TODO: if a 3x3 matrix is passed convert it to a (4x4) transform matrix with rotation on the z-axis
    #  and translations along the x and y-axis
    if np.shape(transform_matrix) == (4, 4):
        vtk_obj = pv.read(infile)
        vtk_obj.transform(transform_matrix)
        if outfile is None:
            outfile = infile[:-4] + '_3D.vtk'
        pv.save_meshio(outfile, vtk_obj)
    else:
        print('invalid transform matrix')
