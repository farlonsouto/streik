import unittest
import Allocator


class StrikeAllocationTest(unittest.TestCase):
    """ Will cover some allocation scenarios with simple test cases"""

    def test_no_pupils(self):
        pupils_list = []
        with self.assertRaises(Exception):
            Allocator.allocate(pupils_list)

    def test_happiest_path_no_restrictions(self):
        pupils_list = []
        result = Allocator.allocate(pupils_list)
        keys = result.keys()

        allocated_pupils = 0
        for key in keys:
            allocated_pupils += len(result.get(key))

        self.assertEqual(len(pupils_list), allocated_pupils)

    def test_already_sorted_inputs(self):
        original = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertExpected(original, expected)
