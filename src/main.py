import sys
from copystatic import copy_files_recursive
from page_generator import generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Setting up docs directory...")
    copy_files_recursive("static", "docs")

    print(f"Generating pages with basepath: '{basepath}'")
    generate_pages_recursive("content", "template.html", "docs", basepath)

    print("Done!")


if __name__ == "__main__":
    main()