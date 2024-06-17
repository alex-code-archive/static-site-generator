block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


def block_to_block_type(markdown):
    first_char = markdown[0]
    first_three_chars = markdown[:3]
    first_eight_chars = markdown[:8]

    if first_char == "#":
        # Skip first char as already accounted for
        for char in first_eight_chars[1:]:
            if char != "#" and char == " ":
                return block_type_heading

        pass
    elif first__three_chars == "```":
        pass
    elif first_char == ">":
        pass
    elif first_char == "*" or first_char == "-":
        pass
    elif first_char == "1":
        pass
    return block_type_paragraph


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
