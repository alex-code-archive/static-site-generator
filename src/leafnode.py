from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = []
        super().__init__(self.tag, self.value, self.children, self.props)
        pass

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
            return f"<{self.tag} {self.props[0]}"
        return f"<{self.tag}>"
