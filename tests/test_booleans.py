import unittest


class BooleanTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)