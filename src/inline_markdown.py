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
            return old_nodes
        temp = text_node.text
        for image in images:
            split_text = temp.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            temp = split_text[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for text_node in old_nodes:
        links = extract_markdown_links(text_node.text)
        if not links:
            return old_nodes
        temp = text_node.text
        for link in links:
            split_text = temp.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            temp = split_text[1]
    return new_nodes


def text_to_textnodes(text):
    text_nodes = []
    textnode = TextNode(text, text_type_text)
    delimiters = ["*", "`", "**"]

    split = split_nodes_link([textnode])
    split = split_nodes_image(split)

    for delimiter in delimiters:
        text_nodes.append(split_nodes_delimiter(
            split, delimiter, text_type_text))
    print(split)
    return text_nodes
