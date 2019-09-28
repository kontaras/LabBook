import unittest
import tempfile
from app import get_markdown_content


class TestGetMarkdownContents(unittest.TestCase):
    def test_markdown(self):
        with tempfile.NamedTemporaryFile() as fd:
            fd.write(b"Heading")
            fd.flush()
            print(fd.name)
            content = get_markdown_content(fd.name)
            self.assertEqual(content, b"<p>Heading</p>")


if __name__ == '__main__':
    unittest.main()
