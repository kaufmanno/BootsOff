import pyproj
from shapely.ops import transform
from shapely.geometry import Point
from bootsoff.topo import geometry
from bootsoff.utils.symbols import symbols


class Station(Point):
    """
    Station class
        
    """
    
    def __init__(self, label=None, coords=(0, 0, 0), crs='EPSG:4326'):
        """
        Station class
        
        Parameters
        -----------
        label : str
            label of the station, if None is given the label is set to ""

        coords : station coordinates
        """

        super().__init__(coords)
        if label is None:
            label = ''
        self._label = label
        self._marker = symbols['station']
        self._crs = crs

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if not isinstance(value, str):
            pass
        else:
            self._label = value

    @property
    def crs(self):
        return self._crs

    @crs.setter
    def label(self, value):
        if not isinstance(value, str):
            pass
        else:
            self._crs = value.capitalize()

    def to_crs(self, crs):
        """ Transforms the station coordinates into another coordinate reference system

        Parameters
        ----------
        crs : str, default: 'EPSG:4326'
            the pyproj string for the destination projection

        Returns
        -------

        """
        from_crs = pyproj.CRS(self.crs)
        to_crs = pyproj.CRS(crs)
        projection = pyproj.Transformer.from_crs(from_crs, to_crs, always_xy=True).transform
        self.coords = transform(projection, Point(self.coords)).coords

    def plot(self, **kwargs):
        """
        Plots a marker at the station coordinates

        Parameters
        -----------
        show_label: bool, default: False
            Set true to show the station label when plotting the station

        **kwargs : dict
            kwargs to pass to plot_shapely_obj()
        """
        show_label = kwargs.pop('show_label', False)
        defaults = {'marker': self._marker, 'markerfacecolor': (0., 0., 0., 0.), 'markeredgecolor': (0., 0., 0., .5),
                    'linestyle': 'None'}
        for k, v in defaults.items():
            if k not in kwargs.keys():
                kwargs.update({k: v})
        ax = geometry.plot_shapely_obj(obj=self, **kwargs)
        if show_label:
            ax.text(self.x, self.y, self._label)


def fake_function(text='Hello World!'):
    """ 
    Prints and returns a text after capitalizing
    
    Parameters
    ----------
    text : str
              
    Returns
    -------
    text: a text
    
    """

    text = text.capitalize()
    print(text)
    return text
