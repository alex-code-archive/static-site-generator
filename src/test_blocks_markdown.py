import unittest
from blocks_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_type_heading(self):
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_heading)

    def test_block_type_heading2(self):
        md = "######This is not a heading"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, block_type_heading)

    def test_block_type_code(self):
        md = "```This is a code block```"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_code)

    def test_block_type_code2(self):
        md = "```This is not a code block``"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, block_type_code)

    def test_block_type_quote(self):
        md = "> This is a quote\n> So is this"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_quote)

    def test_block_type_ordered_list(self):
        md = "1. This is an ordered list item\n2. This is another ordered list item"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, block_type_ordered_list)

    def test_block_type_ordered_list2(self):
        md = "1. This is an ordered list item\n2.This is another ordered list item"
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type, block_type_ordered_list)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
