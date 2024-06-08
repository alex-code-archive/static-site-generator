from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        """
        Parameters:
        text (str): The text content of the node
        text_type (str): The type of text this node contains, such as "bold" or
        "italic"
        url (str): The URL of the link or image, if the text is a link. Default
        to None if nothing is passed in
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        text_equal = self.text == text_node.text
        text_type_equal = self.text_type == text_node.text_type
        url_equal = self.url == text_node.url

        if text_equal and text_type_equal and url_equal:
            return True
        return False

    def text_node_to_html_node(text_node):
        if text_node.text_type == text_type_text:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == text_type_bold:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == text_type_italic:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == text_type_code:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == text_type_image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
