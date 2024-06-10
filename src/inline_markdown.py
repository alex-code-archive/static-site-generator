from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
import re


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        temp = []
        if type(node) is TextNode:
            split = node.text.split(delimiter)
            length = len(split)
            for i in range(length):
                if split[i] == "":
                    continue
                elif length % 2 == 0:
                    raise ValueError("Closing/opening delimiter not found.")
                elif i % 2 != 0:
                    temp.append(TextNode(split[i], text_type))
                else:
                    # Back to back delimiters
                    temp.append(TextNode(split[i], text_type_text))
        else:
            new_nodes.append(node)
        new_nodes.extend(temp)

        return new_nodes
