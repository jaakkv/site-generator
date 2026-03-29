from textnode import TextNode, TextType
from htmlnode import LeafNode
from copystatic import copy_files_recursive

def main():
    print("Setting up public directory...")
    copy_files_recursive("static", "public")
    print("Done!")


# Standard Python practice to ensure main() only runs if the script is executed directly
if __name__ == "__main__":
    main()