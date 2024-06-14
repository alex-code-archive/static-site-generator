import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        node2 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        self.assertEqual(node1, node2)

    def test_tag_inequality(self):
        node1 = HTMLNode("aa", "blah", ["children"], {"href": "test.com"})
        node2 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_value_inequality(self):
        node1 = HTMLNode("a", "lah", ["children"], {"href": "test.com"})
        node2 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_children_inequality(self):
        node1 = HTMLNode("a", "blah", ["cildren"], {"href": "test.com"})
        node2 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_props_inequality(self):
        node1 = HTMLNode("a", "blah", ["children"], {"href": "est.com"})
        node2 = HTMLNode("a", "blah", ["children"], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_props_to_html_equal(self):
        node1 = HTMLNode(
            "a", "blah", ["children"], {"href": "test.com"}
        ).props_to_html()
        node2 = HTMLNode(
            "a", "blah", ["children"], {"href": "test.com"}
        ).props_to_html()
        return self.assertEqual(node1, node2)

    def test_props_to_html_not_equal(self):
        node1 = HTMLNode("a", "blah", ["children"], {
                         "href": "est.com"}).props_to_html()
        node2 = HTMLNode(
            "a", "blah", ["children"], {"href": "test.com"}
        ).props_to_html()
        return self.assertNotEqual(node1, node2)

    def test_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        as_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        return self.assertEqual(node.to_html(), as_html)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
