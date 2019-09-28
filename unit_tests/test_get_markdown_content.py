import unittest
import tempfile
import os
from app import get_markdown_content


class TestGetMarkdownContents(unittest.TestCase):
    def test_markdown(self):
        fd = tempfile.mkstemp()
        try:
            with open(fd[1], "w") as writable:
                writable.write("Heading")
                writable.flush()
            content = get_markdown_content(fd[1])
            self.assertEqual(content, b"<p>Heading</p>")
        finally:
            os.close(fd[0])
            os.unlink(fd[1])


if __name__ == '__main__':
    unittest.main()
