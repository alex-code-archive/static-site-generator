class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        """Render a leaf node as an HTML string. If leaf node has no `value`, raise 
        a ValueError. All leaf nodes require a value.

        Returns:
        (str): Leaf node as an HTML string
        """
        if not self.value:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return f"{self.value}"
        if self.props:
            key = next(iter(self.props))
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        self.tag = tag
        self.value = None
        self.props = props
        self.children = children
        super().__init__(self.tag, self.value, self.children, self.props)

    def to_html(self):
        """Render a leaf node as an HTML string. If leaf node has no `value`, raise
        a ValueError. All leaf nodes require a value.

        Returns:
        (str): Leaf node as an HTML string
        """
        if not self.tag:
            raise ValueError("All leaf nodes require a tag.")
        if self.children is None:
            raise ValueError("No children detected.")

        html = ""

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
