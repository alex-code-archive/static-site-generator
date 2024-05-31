import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_inequality(self):
        node = TextNode("This is a test", "bold")
        node2 = TextNode("This  is a test", "bold")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a test", "bold", None)
        node2 = TextNode("This is a test", "bold")
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a test", "italic")
        node2 = TextNode("This is a test", "bold")
        self.assertNotEqual(node, node2)

    def test_different_urls(self):
        node = TextNode("This is a test", "bold", "test.com")
        node2 = TextNode("This is a test", "bold", "tst.com")
        self.assertNotEqual(node, node2)

    def test_same_urls(self):
        node = TextNode("This is a test", "bold", "test.com")
        node2 = TextNode("This is a test", "bold", "test.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
