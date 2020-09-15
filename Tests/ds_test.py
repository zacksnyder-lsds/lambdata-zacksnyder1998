import unittest
from lambdata.ds import enlarge

class DsTest(unittest.TestCase):
    def enlarge_test(self):
        en = enlarge(5)
        self.assertEqual(en, 500)
