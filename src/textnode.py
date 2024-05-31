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

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
