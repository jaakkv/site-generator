import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        """Tests that nodes with matching URLs are equal."""
        node = TextNode("Click here", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Click here", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        """Tests that different text content makes nodes unequal."""
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is different text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        """Tests that different TextTypes make nodes unequal."""
        node = TextNode("Formatting matters", TextType.BOLD)
        node2 = TextNode("Formatting matters", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none_vs_string(self):
        """Tests that a node with a URL is not equal to one without."""
        node = TextNode("Link node", TextType.LINK, "https://google.com")
        node2 = TextNode("Link node", TextType.LINK, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()