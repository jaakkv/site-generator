import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
            blocks,
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        markdown = """
This is a paragraph.



This is another paragraph with too much space above it.
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "This is a paragraph.",
                "This is another paragraph with too much space above it.",
            ],
            blocks,
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\nprint('hello world')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">This is a quote\n> It spans multiple lines\n>And is very profound"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "This is just a normal paragraph.\nIt has multiple lines, but no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_heading_fallback(self):
        block = "###This is not a valid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_ordered_list_fallback(self):
        block = "1. First\n3. Third\n4. Fourth"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_quote_fallback(self):
        block = ">Quote line 1\nOops no bracket here\n>Quote line 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()