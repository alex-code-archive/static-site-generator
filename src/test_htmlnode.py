import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        node2 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        self.assertEqual(node1, node2)

    def test_tag_inequality(self):
        node1 = HTMLNode('aa', 'blah', ['children'], {"href": "test.com"})
        node2 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_value_inequality(self):
        node1 = HTMLNode('a', 'lah', ['children'], {"href": "test.com"})
        node2 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_children_inequality(self):
        node1 = HTMLNode('a', 'blah', ['cildren'], {"href": "test.com"})
        node2 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_props_inequality(self):
        node1 = HTMLNode('a', 'blah', ['children'], {"href": "est.com"})
        node2 = HTMLNode('a', 'blah', ['children'], {"href": "test.com"})
        self.assertNotEqual(node1, node2)

    def test_props_to_html_equal(self):
        node1 = HTMLNode('a', 'blah', ['children'], {
                         "href": "test.com"}).props_to_html()
        node2 = HTMLNode('a', 'blah', ['children'], {
                         "href": "test.com"}).props_to_html()
        return self.assertEqual(node1, node2)

    def test_props_to_html_not_equal(self):
        node1 = HTMLNode('a', 'blah', ['children'], {
                         "href": "est.com"}).props_to_html()
        node2 = HTMLNode('a', 'blah', ['children'], {
                         "href": "test.com"}).props_to_html()
        return self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
