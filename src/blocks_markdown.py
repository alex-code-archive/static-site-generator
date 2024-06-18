from htmlnode import HTMLNode, ParentNode, LeafNode

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
    return LeafNode("blockquote", markdown.strip(">"))


def convert_unordered_list_to_html(markdown):
    return


def markdown_to_html_node(markdown):
    nodes = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        temp = []
        for line in block.split("\n"):
            if block_type == block_type_quote:
                nodes.append(convert_quote_block_to_html(line))
            elif block_type == block_type_unordered_list:
                temp.append(LeafNode("li", line.strip("*")))
                print(line)
                pass
            elif block_type == block_type_ordered_list:
                pass
            elif block_type == block_type_code:
                pass
            elif block_type == block_type_heading:
                pass
            elif block_type == block_type_paragraph:
                pass
            for line in block.split("\n"):
                pass
    print(nodes)
    # TODO: With the block types, loop through the list of blocks and convert to html nodes
    # Will need to split on \n character
    convert_quote_block_to_html(markdown)
