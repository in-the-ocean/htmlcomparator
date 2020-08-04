import unittest
import sys
sys.path.append("../")
from htmlcomparator.html_comparator import HTMLComparator

class TestHTMLComparator(unittest.TestCase):
    def test_compare_files_1(self):
        s1 = "<html><head><title>Test</title></head>"
        s2 = "<html><head><title>Test</title></head>"
        comparator = HTMLComparator()
        self.assertTrue(comparator.compare_files(s1,s2))

    def test_compare_files_2(self):
        s1 = "<html><div><title>Test</title></div>"
        s2 = "<html><head><title>Test</title></head>"
        comparator = HTMLComparator()
        self.assertFalse(comparator.compare_files(s1,s2))

    def test_compare_files_3(self):
        pass

    def test_compare_files_4(self):
        pass

if __name__ == "__main__":
    unittest.main()