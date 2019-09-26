import unittest
import app
import tempfile


class TestGetSubPages(unittest.TestCase):
    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_file(self):
        with tempfile.NamedTemporaryFile(mode="x") as tmp_file:
            self.assertListEqual(app.get_sub_pages(tmp_file.name), [])


if __name__ == "__main__":
    unittest.main()
