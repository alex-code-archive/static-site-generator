import functools


class HTMLNode:
    def __init__(self, tag, value, children, props):
        """
        Parameters:
        tag (str): A string representing the HTML tag name (e.g. 'p', 'a',
        'h1', etc)

        value (str): A string representing the value of the HTML tag (e.g. text
        inside paragraph)

        children (list): A list of HTMLNode objects representing the children
        of this node

        props (dict): A dictionary of key-value pairs representing the
        attributes of the HTML tag. E.g., a link (<a> tag) might have {"href":
        "https://www.google.com"}

        All will default to None
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other_html_node):
        tag_match = self.tag == other_html_node.tag
        value_match = self.value == other_html_node.value
        children_match = self.children == other_html_node.children
        props_match = self.props == other_html_node.props

        if tag_match and value_match and children_match and props_match:
            return True
        return False

    def __repr__(self):
        return f"\nTag={self.tag}\nValue={self.value}\nChildren={self.children}\nProps={self.props}\n"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        for key, value in self.props.items():
            html += f'{key}="{value}" '
        return html
