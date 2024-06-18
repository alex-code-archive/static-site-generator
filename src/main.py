from blocks_markdown import (
    # markdown_to_blocks,
    # block_to_block_type,
    markdown_to_html_node,
)


def main():
    md = """
>This is a block quote\n>This is another one\n\n* This is an unordered list\n* This is another one\n\n
1. This is an ordered list\n2. This is another one\n\n```This is a code block```\n\n
# This is a heading\n###### This is the smallest heading\n\n
This is a paragraph
    """
    markdown_to_html_node(md)


if __name__ == "__main__":
    main()
