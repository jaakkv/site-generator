from textnode import TextNode, TextType


def main():
    # Creating a dummy node with a link
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    # Printing the node to trigger the __repr__ method
    print(node)


# Standard Python practice to ensure main() only runs if the script is executed directly
if __name__ == "__main__":
    main()