from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_code,
    text_type_italic,
    text_type_bold,
)
import re
from pprint import pprint


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for text_node in old_nodes:
        images = extract_markdown_images(text_node.text)
        if not images:
            new_nodes.append(text_node)
        temp = text_node.text
        for image in images:
            split_text = temp.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            new_nodes.append(TextNode(split_text[1], text_type_text))
            temp = split_text[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for text_node in old_nodes:
        links = extract_markdown_links(text_node.text)
        if not links:
            new_nodes.append(text_node)
        temp = text_node.text
        for link in links:
            split_text = temp.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            new_nodes.append(TextNode(split_text[1], text_type_text))
            temp = split_text[1]
    return new_nodes


def text_to_textnodes(text):
    text_nodes = [TextNode(text, text_type_text)]
    delimiters = {"*": text_type_italic, "`": text_type_code, "**": text_type_bold}

    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    # for delimiter, text_type in delimiters.items():
    #     text_nodes.append(split_nodes_delimiter(
    #         text_nodes, delimiter, text_type))
    pprint(text_nodes)
    return text_nodes
