"Tests for the get_markdown_content method"

import unittest
import tempfile
import os
from app import get_markdown_content


class TestGetMarkdownContents(unittest.TestCase):
    "Tests for the get_markdown_content method"
    def test_markdown(self):
        """
        Basic test.
        Tests that if markdown is passed in, HTML comes out
        """
        file_disc = tempfile.mkstemp()
        try:
            with open(file_disc[1], "w") as writable:
                writable.write("Heading")
                writable.flush()
            content = get_markdown_content(file_disc[1])
            self.assertEqual(content, b"<p>Heading</p>")
        finally:
            os.close(file_disc[0])
            os.unlink(file_disc[1])


if __name__ == '__main__':
    unittest.main()
