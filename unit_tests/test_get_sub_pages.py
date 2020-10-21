"""Tests for the get_sub_pages function."""

import unittest
import tempfile
import os
import app


DEFAULT_PAGE = "pindex"


class TestGetSubPages(unittest.TestCase):
    """Tests for the get_sub_pages function."""
    def test_empty_dir(self):
        """
        Test an empty directory.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_file(self):
        """
        Test a directory with a file.
        """
        with tempfile.NamedTemporaryFile(mode="x") as tmp_file:
            self.assertListEqual(app.get_sub_pages(tmp_file.name), [])

    def test_dir_only_index(self):
        """
        Test a directory with an index.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "index.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_dir_non_md(self):
        """
        Test a directory with an invalid file.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "valid.txt"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), [])

    def test_dir_with_file(self):
        """
        Test a directory with a file.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, DEFAULT_PAGE + ".md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), [DEFAULT_PAGE])

    def test_dir_with_files(self):
        """
        Test a directory with multiple files.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, DEFAULT_PAGE + ".md"), "x").close()
            open(os.path.join(tmp_dir, DEFAULT_PAGE + "2.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir),
                                 [DEFAULT_PAGE, DEFAULT_PAGE + "2"])

    def test_dir_with_sub_dir(self):
        """
        Test a directory with a sub-directory.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, DEFAULT_PAGE))
            self.assertListEqual(app.get_sub_pages(tmp_dir), [DEFAULT_PAGE])

    def test_dir_with_sub_dirs(self):
        """
        Test a directory with multiple sub-directories.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, DEFAULT_PAGE))
            os.mkdir(os.path.join(tmp_dir, DEFAULT_PAGE + "2"))
            self.assertListEqual(app.get_sub_pages(tmp_dir),
                                 [DEFAULT_PAGE, DEFAULT_PAGE + "2"])

    def test_dir_with_dir_and_file(self):
        """
        Test a directory with a sub-directory and a file.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "dir"))
            open(os.path.join(tmp_dir, DEFAULT_PAGE + ".md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["dir",
                                                              DEFAULT_PAGE])

    def test_dir_with_dir_file_and_junk(self):
        """
        Test a directory with a sub-directory, a file, an invalid file, and an
        index.
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.mkdir(os.path.join(tmp_dir, "dir"))
            open(os.path.join(tmp_dir, DEFAULT_PAGE + ".md"), "x").close()
            open(os.path.join(tmp_dir, "valid.txt"), "x").close()
            open(os.path.join(tmp_dir, "index.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["dir",
                                                              DEFAULT_PAGE])


if __name__ == "__main__":
    unittest.main()
