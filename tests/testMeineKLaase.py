import unittest
from meineklasse import meineklasse
class testMeineKLaase(unittest.TestCase):
    def setUp(self):
        self.obj = meineklasse()

    def test_initial_value(self):
        self.assertEqual(self.obj.x, 100)
    def test_set_value(self):
        self.obj.x = 250
        self.assertEqual(self.obj.x, 250)