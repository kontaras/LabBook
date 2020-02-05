import unittest
from utils import run_page


class Test(unittest.TestCase):

    def testName(self):
        run_page("a", "http://foo")


if __name__ == "__main__":
    unittest.main()
