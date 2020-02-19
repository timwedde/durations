import unittest

from durations_nlp.scales import Scale


class TestScale(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_repr(self):
        self.assertEqual(Scale("d").__repr__(), "<Scale day>")

    def test_str(self):
        self.assertEqual(Scale("d").__str__(), "<Scale day>")
