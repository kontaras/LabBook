"""
Pages ending in "md" would not show up in sub-pages
"""

import unittest
import tempfile
import os
from pathlib import Path
import app


class TestRegressionSubpagesEndingMd(unittest.TestCase):
    """Test that pages ending in md show up correctly in subpages"""
    def test(self):
        """
        Replicate the regression
        """
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_file = Path(os.path.join(tmp_dir, "namemd.md"))
            tmp_file.touch()
            self.assertListEqual(app.get_sub_pages(tmp_dir), ["namemd"])
