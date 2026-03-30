import unittest
from page_generator import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_with_whitespace(self):
        self.assertEqual(extract_title("   \n#   Hello World  \n  "), "Hello World")

    def test_extract_title_no_h1(self):
        with self.assertRaises(ValueError):
            extract_title("## This is an H2\nNormal text")


if __name__ == "__main__":
    unittest.main()