from shapely.geometry import Point
from bootsoff.utils.topo import geometry
from bootsoff.utils.topo import symbols


class Station(Point):
    """
    Station class
    
    Attributes
    -----------
    label : str
        
    """
    
    def __init__(self, label=None, coords=(0,0,0)):
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

    @property
    def label(self):
        return self._name

    @label.setter
    def label(self, value):
        if not isinstance(value, str):
            pass
        else:
            self._label = value

    def plot(self, **kwargs):
        marker = symbols.symbols['station']
        geometry.plot_shapely_obj(obj=self, **kwargs)

    def display(self, text=None):
        """
        Displays a text or name attribute if text is None
        
        Parameters
        -----------
        text : str
            if None, displays name (default=None)
        """
        
        if text is None:
            print(self.name)
        else:
            print(text)


def fake_function(text='Hello World!'):
    """ 
    Prints and returns a text after capitalizing
    
    Parameters
    ----------
    name : str
              
    Returns
    -------
    text: a text
    
    """

    text = text.capitalize()
    print(text)
    return text

