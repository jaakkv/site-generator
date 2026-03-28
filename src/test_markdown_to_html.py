import unittest
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraphs(self):
        # Using \n for newlines so nothing gets lost in translation
        md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with *italic* text and `code` here"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = "- This is a list\n- with items\n- and *more* items\n\n1. This is an `ordered` list\n2. with items\n3. and more items"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()