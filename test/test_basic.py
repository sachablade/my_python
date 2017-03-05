import unittest
from utils.bs4_utils import Bs4

class Bs4TestSuite(unittest.TestCase):
    """Basic test cases for Bs4."""

    @staticmethod
    def test_class_definition():
        obj = Bs4('http://www.newpct1.com/series-hd/666-park-avenue/1582')
        assert obj.encoding=='iso-8859-1'

class BasicTestSuite2(unittest.TestCase):
    """Basic test cases."""

    @staticmethod
    def test_absolute_truth_and_meaning():
        print 'asd2'
        assert True

if __name__ == '__main__':
    unittest.main()