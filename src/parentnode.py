from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        self.tag = tag
        self.value = None 
        self.props = props
        self.children = children
        super().__init__(self.tag, self.value, self.children, self.props)

    def __eq__(self, other_leaf):
        tag_equal = self.tag == other_leaf.tag
        value_equal = self.value == other_leaf.value
        props_equal = self.props == other_leaf.props
        children_equal = self.children == other_leaf.children

        if tag_equal and value_equal and props_equal and children_equal:
            return True
        return False

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
        if self.props:
            key = next(iter(self.props))
            return f'<{self.tag} {key}="{self.props[key]}">{self.value}</{self.tag}>'

        return f"<{self.tag}>{self.value}</{self.tag}>"
