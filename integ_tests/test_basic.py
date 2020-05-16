"A few tests to verify that the server serves pages correctly."

import unittest
from utils import run_page


class BasicTest(unittest.TestCase):
    "Tests for basic page contents"

    def test_contents(self):
        "Test that the page contains the document contents"
        parts = run_page({"bar": "got it"}, "bar")
        self.assertEqual(parts["contents"], "<p>got it</p>")


if __name__ == "__main__":
    unittest.main()
