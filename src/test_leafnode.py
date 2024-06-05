import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf1 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        leaf2 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        self.assertEqual(leaf1, leaf2)

    def test_diff_tag(self):
        leaf1 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        leaf2 = LeafNode('b', 'A link here', {'href': 'www.test.com'})
        self.assertNotEqual(leaf1, leaf2)

    def test_diff_value(self):
        leaf1 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        leaf2 = LeafNode('a', 'B link here', {'href': 'www.test.com'})
        self.assertNotEqual(leaf1, leaf2)

    def test_diff_props(self):
        leaf1 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        leaf2 = LeafNode('a', 'A link here', {'href': 'www.test.co'})
        self.assertNotEqual(leaf1, leaf2)

    def test_to_html(self):
        leaf1 = LeafNode('a', 'A link here', {'href': 'www.test.com'})
        leaf2 = LeafNode('img', 'B link here', {'src': 'www.test.co'})

        leaf1_html = '<a href="www.test.com">A link here</a>'
        leaf2_html = '<img src="www.test.co">B link here</img>'
        self.assertEqual(leaf1.to_html(), leaf1_html)
        self.assertEqual(leaf2.to_html(), leaf2_html)

    def test_to_html_no_props(self):
        leaf1 = LeafNode('a', 'A link here', {})
        leaf2 = LeafNode('img', 'B link here', {})

        leaf1_html = '<a>A link here</a>'
        leaf2_html = '<img>B link here</img>'
        self.assertEqual(leaf1.to_html(), leaf1_html)
        self.assertEqual(leaf2.to_html(), leaf2_html)
