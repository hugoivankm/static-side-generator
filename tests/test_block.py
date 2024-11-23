import unittest
from src.block import Block, BlockType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = Block("This is a paragraph", BlockType.PARAGRAPH)
        node2 = Block("This is a paragraph", BlockType.PARAGRAPH)
        self.assertEqual(node1, node2)

        node1 = Block("###This is a heading", BlockType.HEADING)
        node2 = Block("###This is a heading", BlockType.HEADING)

    def test_not_eq(self):
        node1 = Block(
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item", BlockType.UNORDERED_LIST)
        node2 = Block(
            "* This is the first list item in a list block\n This is a list item\n*This is another list item", BlockType.UNORDERED_LIST)
        self.assertNotEqual(node1, node2)

    def test_repr__(self):
        self.assertEqual(Block("> This is a quote", BlockType.QUOTE).__repr__(
        ), 'Block("> This is a quote", "BlockType.QUOTE")')

    def test_block_to_block_type(self):
        heading_text = "# This is a heading"
        actual = Block.block_to_block_type(heading_text)
        expected = "heading"
        self.assertEqual(actual, expected)

        paragraph_text = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        actual = Block.block_to_block_type(paragraph_text)
        expected = "paragraph"
        self.assertEqual(actual, expected)

        ordered_list = "1. First Item\n2. Second Item\n3. Third Item"
        actual = Block.block_to_block_type(ordered_list)
        expected = "ordered list"
        self.assertEqual(actual, expected)
        
        
        unordered_list = "* First Item\n* Second Item\n* Third Item"
        actual = Block.block_to_block_type(unordered_list)
        expected = "unordered list"
        self.assertEqual(actual, expected)
