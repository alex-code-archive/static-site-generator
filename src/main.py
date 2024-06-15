from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)
from blocks_markdown import markdown_to_blocks
from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

from pprint import pprint


def main():
    print( markdown_to_blocks("""This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items""" ))


if __name__ == "__main__":
    main()
