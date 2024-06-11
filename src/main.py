from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
)
from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode


def main():
    # print(TextNode('This is a text node', 'bold', 'https://www.boot.dev'))
    # test = HTMLNode('a', 'none', [], {
    #                 'href': 'https://www.google.com', 'target': 'blank'})
    # test.props_to_html()
    # print(LeafNode('a', 'Link here', {'href': 'www.test.com'}).to_html())
    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )
    # print(node)
    # print(node.to_html())
    # node = TextNode("This is text with a `code block``ligma` word", "text")
    # new_node = split_nodes_delimiter([node], "`", "code")
    # print(new_node)
    # text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    # print(extract_markdown_images(text))
    # text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text))
    # node = TextNode(
    #     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    #     "text",
    # )
    # new_nodes = split_nodes_image([node])
    # print(new_nodes)


if __name__ == "__main__":
    main()
