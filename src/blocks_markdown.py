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
    split_text = markdown.split("\n")
    block_type = block_type_paragraph

    if first_char == "#":
        # Skip first char as already accounted for
        for char in first_eight_chars[1:]:
            if char != "#" and char == " ":
                block_type = block_type_heading

    elif first_three_chars == "```":
        if markdown[-3:] == "```":
            block_type = block_type_code
    elif first_char == ">":
        block_type = block_type_quote
        for line in split_text[1:]:
            if line[0] != ">":
                block_type = block_type_paragraph
    elif first_char == "*" or first_char == "-":
        block_type = block_type_unordered_list
        for line in split_text[1:]:
            if line[1] != " ":
                block_type = block_type_paragraph
    elif first_char == "1":
        num = 2
        block_type = block_type_ordered_list
        for line in split_text[1:]:
            if line[:3] != f"{num}. ":
                block_type = block_type_paragraph
    return block_type


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def convert_quote_block_to_html(markdown):
    pass
    # for block in blocks:
    #     print(block)


def markdown_to_html_node(markdown):
    block_types = []
    nodes = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_types.append(block_to_block_type(block))
    print(block_types)
    # TODO: With the block types, loop through the list of blocks and convert to html nodes
    # Will need to split on \n character
    convert_quote_block_to_html(markdown)
