from copystatic import copy_files_recursive
from page_generator import generate_pages_recursive


def main():
    print("Setting up public directory...")
    copy_files_recursive("static", "public")

    print("Generating pages...")
    generate_pages_recursive("content", "template.html", "public")

    print("Done!")


if __name__ == "__main__":
    main()