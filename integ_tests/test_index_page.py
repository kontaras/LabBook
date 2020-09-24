'''
tests that index pages are properly found
'''
import unittest
from utils import run_page


class Test(unittest.TestCase):
    '''
    tests that index pages are properly found
    '''

    def test_root(self):
        "Test that the root path"
        parts = run_page({"index": "the root index"}, "")
        self.assertEqual(parts["contents"], "<p>the root index</p>")

    def test_dir(self):
        "Test directory index"
        parts = run_page({"index": "the root index",
                          "dir/index": "the dir index"}, "dir")
        self.assertEqual(parts["contents"], "<p>the dir index</p>")


if __name__ == "__main__":
    unittest.main()
