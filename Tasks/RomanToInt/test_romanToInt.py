import unittest
import romanToInt

class TestRomanToInt(unittest.TestCase):
    def test_romantoint(self):
        self.assertEqual(romanToInt.romanToInt("XVI"), 16)
        self.assertEqual(romanToInt.romanToInt("LV"), 55)
        self.assertNotEqual(romanToInt.romanToInt("X"), 1)
        self.assertEqual(romanToInt.romanToInt("MCDXVI"), 1416)
        with self.assertRaises(Exception):
            romanToInt.romanToInt("")

    def test_romantointv2(self):
        self.assertEqual(romanToInt.romanToIntv2("XVI"), 16)
        self.assertEqual(romanToInt.romanToIntv2("LV"), 55)
        self.assertNotEqual(romanToInt.romanToIntv2("X"), 1)
        self.assertEqual(romanToInt.romanToIntv2("MCDXVI"), 1416)