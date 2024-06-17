from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)
from blocks_markdown import markdown_to_blocks, block_to_block_type
from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

from pprint import pprint


def main():
    block_to_block_type(
        "1. This is an ordered list item\n2. This is another ordered list item"
    )


if __name__ == "__main__":
    main()
