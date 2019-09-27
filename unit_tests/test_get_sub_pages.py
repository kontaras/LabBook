import unittest
import app
import tempfile
import os


class TestGetSubPages(unittest.TestCase):
    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_file(self):
        with tempfile.NamedTemporaryFile(mode="x") as tmp_file:
            self.assertListEqual(app.get_sub_pages(tmp_file.name), [])

    def test_dir_only_index(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "index.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_dir_non_md(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "valid.txt"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_dir_with_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "pindex.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["pindex"])

    def test_dir_with_files(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "pindex.md"), "x").close()
            open(os.path.join(tmp_dir, "pindex2.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["pindex",
                                                              "pindex2"])

    def test_dir_with_sub_dir(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "pindex"))
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["pindex"])

    def test_dir_with_sub_dirs(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "pindex"))
            os.mkdir(os.path.join(tmp_dir, "pindex2"))
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["pindex",
                                                              "pindex2"])

    def test_dir_with_dir_and_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "dir"))
            open(os.path.join(tmp_dir, "pindex.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["dir", "pindex"])

    def test_dir_with_dir_file_and_junk(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "dir"))
            open(os.path.join(tmp_dir, "pindex.md"), "x").close()
            open(os.path.join(tmp_dir, "valid.txt"), "x").close()
            open(os.path.join(tmp_dir, "index.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["dir", "pindex"])


if __name__ == "__main__":
    unittest.main()
