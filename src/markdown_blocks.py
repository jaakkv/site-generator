from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    clean_blocks = []
    for block in raw_blocks:
        stripped_block = block.strip()

        if stripped_block == "":
            continue

        clean_blocks.append(stripped_block)

    return clean_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if len(block) >= 6 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_ulist = True
    for line in lines:
        if not line.startswith("- "):
            is_ulist = False
            break
    if is_ulist:
        return BlockType.UNORDERED_LIST

    is_olist = True
    for i, line in enumerate(lines):
        expected_start = f"{i + 1}. "
        if not line.startswith(expected_start):
            is_olist = False
            break
    if is_olist:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH