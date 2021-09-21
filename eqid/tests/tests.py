from unittest import TestCase

import eqid


class TestEarthquake(TestCase):
    def test_contains_complete_key(self):
        result = eqid.get_data()

        self.assertIn('date', result)
        self.assertIn('time', result)
        self.assertIn('magnitude', result)
        self.assertIn('depth', result)
        self.assertIn('location', result)
        self.assertIn('center_desc', result)
        self.assertIn('desc', result)
