from copystatic import copy_files_recursive
from page_generator import generate_page


def main():
    print("Setting up public directory...")
    copy_files_recursive("static", "public")

    print("Generating pages...")
    generate_page("content/index.md", "template.html", "public/index.html")

    print("Done!")


if __name__ == "__main__":
    main()