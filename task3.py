import math
import unittest


def to_cyclic(time):
    angle = (time / 24) * 2 * math.pi
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)
    return [sin_val, cos_val]


def time_difference(time1, time2):
    time1_cyclic = to_cyclic(time1)
    time2_cyclic = to_cyclic(time2)

    dot_product = time1_cyclic[0] * time2_cyclic[0] + time1_cyclic[1] * time2_cyclic[1]
    return math.acos(dot_product) * (24 / (2 * math.pi))


# Unit tests for the time functions
class TestTimeTransformation(unittest.TestCase):

    def test_time_difference_same_time(self):
        # Time difference between two identical times should be 0 hours
        self.assertEqual(time_difference(5, 5), 0)

    def test_time_difference_24_hours(self):
        # Time difference between 00:00 and 00:00 should be 0 hours
        self.assertEqual(time_difference(0, 24), 0)

    def test_time_difference_half_day(self):
        # Time difference between 00:00 and 12:00 should be exactly 12 hours
        self.assertEqual(time_difference(0, 12), 12)

    def test_time_difference_across_midnight(self):
        # Time difference between 23:00 (current day) and 01:00 (next day) should be 2 hours
        self.assertAlmostEqual(time_difference(23, 1), 2, places=1)

    def test_time_difference_close_times(self):
        # Time difference between 23:00 and 23:59 should be small but positive
        self.assertAlmostEqual(time_difference(23, 23.9833), 0.9833, places=1)

    def test_time_difference_full_cycle(self):
        # Time difference between 0:00 and 24:00 should be 0 hours due to cyclic nature
        self.assertEqual(time_difference(0, 24), 0)

    def test_time_difference_opposite_times(self):
        # Time difference between 06:00 and 18:00 should be 12 hours
        self.assertEqual(time_difference(6, 18), 12)


if __name__ == '__main__':
    unittest.main()
