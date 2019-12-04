"""Tests for the generate_breadcrumb method"""

import unittest
from app import generate_breadcrumb


class TestGenerateBreadcrumb(unittest.TestCase):
    """Tests for the generate_breadcrumb method"""
    def test_file_in_root(self):
        """Test a file in the root directory"""
        self.assertListEqual(generate_breadcrumb("/something"),
                             [("Home", "/")])

    def test_file_in_dir(self):
        """Test a file in a directory"""
        target = [("Home", "/"),
                  ("parent", "/parent")]
        self.assertListEqual(generate_breadcrumb("/parent/something"),
                             target)

    def test_file_in_multi_dir(self):
        """Test a file in a directory in a directory"""
        target = [("Home", "/"),
                  ("parent", "/parent"),
                  ("subparent", "/parent/subparent")]
        page_path = "/parent/subparent/something"
        self.assertListEqual(generate_breadcrumb(page_path), target)

    def test_root(self):
        """Tests getting a breadcrumb for root"""
        self.assertListEqual(generate_breadcrumb(""), [("Home", "/")])


if __name__ == '__main__':
    unittest.main()
