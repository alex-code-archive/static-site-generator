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


def convert_quote_block_to_html(block):
    return map(lambda line: LeafNode("blockquote", line.strip(">")), block.split("\n"))


def convert_unordered_list_to_html(block):
    return [
        ParentNode(
            "ul",
            list(
                map(lambda line: LeafNode(
                    "li", line.lstrip("*-")), block.split("\n"))
            ),
        )
    ]


def convert_ordered_list_to_html(block):
    nodes = []
    split = block.split("\n")
    for i in range(len(split)):
        nodes.append(LeafNode("li", split[i].strip(f"{i + 1}. ")))
    return [ParentNode("ol", nodes)]


def convert_code_block_to_html(block):
    leaf_node = LeafNode("code", block.strip("`"))
    parent_node = [ParentNode("pre", [leaf_node])]
    return parent_node


def convert_heading_block_to_html(block):
    nodes = map(
        lambda line: LeafNode(f"h{line.count('#')}", line.strip("# ")),
        block.split("\n"),
    )
    return list(nodes)


def convert_paragraph_block_to_html(block):
    return


def markdown_to_html_node(markdown):
    nodes = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_quote:
            nodes.extend(convert_quote_block_to_html(block))
        elif block_type == block_type_unordered_list:
            nodes.extend(convert_unordered_list_to_html(block))
        elif block_type == block_type_ordered_list:
            nodes.extend(convert_ordered_list_to_html(block))
        elif block_type == block_type_code:
            nodes.extend(convert_code_block_to_html(block))
        elif block_type == block_type_heading:
            nodes.extend(convert_heading_block_to_html(block))
        elif block_type == block_type_paragraph:
            pass
    print(nodes)
    return ParentNode("div", nodes)
