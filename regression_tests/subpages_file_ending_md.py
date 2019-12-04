"""
Pages ending in "md" would not show up in sub-pages
"""

import unittest
import tempfile
import os
import app


class TestRegressionSubpagesEndingMd(unittest.TestCase):
    """Test that pages ending in md show up correctly in subpages"""
    def test(self):
        """
        Replicate the regression
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            open(os.path.join(tmp_dir, "namemd.md"), "x").close()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["namemd"])