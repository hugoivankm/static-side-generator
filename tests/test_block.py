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
        node1 = Block("* This is the first list item in a list block\n* This is a list item\n* This is another list item", BlockType.UNORDERED_LIST)
        node2 = Block("* This is the first list item in a list block\n This is a list item\n*This is another list item", BlockType.UNORDERED_LIST)
        self.assertNotEqual(node1, node2)
        
    def test_repr__(self):
        return (Block("> This is a quote", BlockType.QUOTE).__repr__ == 'Block("{> This is a quote"}", "{BlockType.QUOTE}")')
