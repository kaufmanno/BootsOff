import unittest
from .context import bootsoff

from shapely.geometry import Point


class CoreTestCase(unittest.TestCase):
    def test_fake_function(self):
        actual = bootsoff.core.fake_function()
        expected = "Hello world!"
        self.assertEqual(expected, actual)

    def test_station_class(self):
        station = bootsoff.Station(label='test');
        actual = station.label
        expected = 'test'
        self.assertEqual(expected, actual)
        actual = [i for i in station.coords]
        expected = [i for i in Point(0., 0., 0.).coords]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
