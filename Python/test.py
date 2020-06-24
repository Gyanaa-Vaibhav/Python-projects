import unittest
from Testing import Practice


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = Practice.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param2 = 'sdf'
        result = Practice.do_stuff(test_param2)
        self.assertFalse(isinstance(result, TypeError))


unittest.main()
