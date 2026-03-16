import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        """Tests that a single property is formatted correctly."""
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        """Tests that multiple properties are formatted with correct spacing."""
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_none(self):
        """Tests that a node with no props returns an empty string."""
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()