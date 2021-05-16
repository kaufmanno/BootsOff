import unittest
from .context import bootsoff


class UtilsTestCase(unittest.TestCase):
    def test_is_sorted_list_numeric(self):
        asc_sorted_list = [3., 7., 11.5, 99.1]
        actual = bootsoff.utils.ordered.is_sorted(asc_sorted_list)
        expected = True
        self.assertEqual(actual, expected)
        desc_sorted_list = [99.1, 11.5, 7., 3.]
        actual = bootsoff.utils.ordered.is_sorted(desc_sorted_list, ascending=False)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_sorted_list_strings(self):
        asc_sorted_list = ['A', 'B', 'C', 'E']
        actual = bootsoff.utils.ordered.is_sorted(asc_sorted_list)
        expected = True
        self.assertEqual(actual, expected)
