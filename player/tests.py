import unittest
from test import test_support

class TestCase1(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        assert(True)

def test_main():
    test_support.run_unittest(TestCase1,)

if __name__ == '__main__':
    test_main()
