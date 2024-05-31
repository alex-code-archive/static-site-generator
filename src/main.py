from textnode import TextNode
from htmlnode import HTMLNode


def main():
    print(TextNode('This is a text node', 'bold', 'https://www.boot.dev'))
    test = HTMLNode('a', 'none', [], {
                    'href': 'https://www.google.com', 'target': 'blank'})
    test.props_to_html()
    print(test)


if __name__ == "__main__":
    main()
