import unittest
import numpy as np
from shapely.geometry import Point
from .context import bootsoff


class TopoTestCase(unittest.TestCase):
    def test_ddmm_to_dd(self):
        ddmm_angle = 6030.
        actual = bootsoff.topo.ddmm_to_dd(ddmm_angle)
        expected = 60.5
        self.assertAlmostEqual(actual, expected, places=12)

    def test_azimuth(self):
        origin = Point(0, 0)
        target = Point(1/2, np.sqrt(3)/2)
        actual = bootsoff.topo.azimuth(origin, target)
        expected = np.pi/6.
        self.assertAlmostEqual(actual, expected, places=12)

    def test_cclength2xz(self):
        known_points = [[0, 284], [58, 280], [152, 275], [217, 270], [228, 267], [305, 265], [340, 260], [374, 255],
                        [397, 250], [417, 245], [459, 240], [484, 245], [539, 250], [687, 245]]
        actual = bootsoff.topo.cclength2xz(known_points, np.linspace(0, 800, 81))[65][0]
        expected = 645.9384090750688
        self.assertAlmostEqual(actual, expected, places=12)
