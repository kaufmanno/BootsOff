import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon
from shapely.affinity import translate, rotate, scale, skew, affine_transform
from descartes import PolygonPatch


class Survey:
    def __init__(self, name):
        self._name = ''
        self.name = name


    @property.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str)
        self._name = value

    def load(self, filename):
        pass

    def plot(self):
        pass

    def save(self, filename):
        pass
