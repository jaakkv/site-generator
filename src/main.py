from textnode import TextNode, TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")


def main():
    # Creating a dummy node with a link
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    # Printing the node to trigger the __repr__ method
    print(node)


# Standard Python practice to ensure main() only runs if the script is executed directly
if __name__ == "__main__":
    main()