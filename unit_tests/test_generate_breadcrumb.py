import unittest
from app import generate_breadcrumb


class MyTestCase(unittest.TestCase):
    def test_file_in_root(self):
        self.assertListEqual(generate_breadcrumb("/something"),
                             [("Home", "/")])

    def test_file_in_dir(self):
        target = [("Home", "/"),
                  ("parent", "/parent")]
        self.assertListEqual(generate_breadcrumb("/parent/something"),
                             target)

    def test_file_in_multi_dir(self):
        target = [("Home", "/"),
                  ("parent", "/parent"),
                  ("subparent", "/parent/subparent")]
        page_path = "/parent/subparent/something"
        self.assertListEqual(generate_breadcrumb(page_path), target)

    def test_root(self):
        self.assertListEqual(generate_breadcrumb(""), [("Home", "/")])


if __name__ == '__main__':
    unittest.main()
