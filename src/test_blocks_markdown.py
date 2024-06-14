import unittest

from blocks_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_block_paragraph(self):
        text = """This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items"""

        split_blocks = markdown_to_blocks(text)
        self.assertListEqual(
            [
                ["This is **bolded** paragraph"],
                [
                    "This is another paragraph with *italic* text and `code` here\n"
                    "    This is the same paragraph on a new line"
                ],
                ["* This is a list\n    * with items"],
            ],
            split_blocks,
        )
