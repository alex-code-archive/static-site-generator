from inline_markdown import split_nodes_delimiter
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
    node = TextNode("This is text with a `code block``ligma` word", "text")
    new_node = split_nodes_delimiter([node], "`", "code")
    print(new_node)


if __name__ == "__main__":
    main()
