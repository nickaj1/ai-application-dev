import unittest

from sum import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)  # When 2 and 4 are given as input the output must be 6.
        self.assertEqual(add(0, 0), 0)  # When 0 and 0 are given as input the output must be 0.
        self.assertEqual(add(2.3, 3.6), 5.9)  # When 2.3 and 3.6 are given as input the output must be 5.9.
        self.assertEqual(add("hello", "world"), "helloworld")  # When the strings ‘hello’ and ‘world’ are given as input the output must be ‘helloworld’.
        self.assertEqual(add(2.300, 4.300), 6.6)  # When 2.3000 and 4.300 are given as input the output must be 6.6.
        self.assertNotEqual(add(-2, -2), 0)  # When -2 and -2 are given as input the output must not be 0.


unittest.main()