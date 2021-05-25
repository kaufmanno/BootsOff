from shapely.geometry import Point
from bootsoff.topo import geometry
from bootsoff.utils.symbols import symbols


class Station(Point):
    """
    Station class
    
    Attributes
    -----------
    label : str
        
    """
    
    def __init__(self, label=None, coords=(0, 0, 0)):
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

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if not isinstance(value, str):
            pass
        else:
            self._label = value

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
        show_label = kwargs.pop('show_label', False)  # TODO: Implement this
        defaults = {'marker': self._marker, 'markerfacecolor': (0., 0., 0., 0.), 'markeredgecolor': (0., 0., 0., .5),
                    'linestyle': 'None'}
        for k, v in defaults.items():
            if k not in kwargs.keys():
                kwargs.update({k: v})
        geometry.plot_shapely_obj(obj=self, **kwargs)


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


def plot_stations(stations):
    """
    Prints and returns a text after capitalizing

    Parameters
    ----------
    stations : list

    Returns
    -------

    """

    text = text.capitalize()
    print(text)
