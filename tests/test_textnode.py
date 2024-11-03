import unittest
from enum import Enum

from src.textnode import TextNode



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    ERROR = "error"

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold", TextType.BOLD)
        node2 = TextNode("This is a bold", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is text", TextType.TEXT)
        self.assertEqual(node, node2)
        
        node = TextNode("This is italic", TextType.ITALIC)
        node2 = TextNode("This is italic", TextType.ITALIC)
        self.assertEqual(node, node2)
                
        node = TextNode("This is code", TextType.CODE)
        node2 = TextNode("This is code", TextType.CODE)
        self.assertEqual(node, node2)

        node = TextNode("image", TextType.IMAGE, "https://picsum.photos/200/300" )
        node2 = TextNode("image", TextType.IMAGE, "https://picsum.photos/200/300" )
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a bol", TextType.BOLD)
        node2 = TextNode("This is a bold", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
        node = TextNode("This is a bol", TextType.ITALIC)
        node2 = TextNode("This is a bold", TextType.BOLD)
        self.assertNotEqual(node, node2)
         
        image1 = TextNode("image", TextType.IMAGE, None)
        image2 = TextNode("image", TextType.IMAGE)
        self.assertNotEqual(image1.__repr__(), image2.__repr__())
    
    def test_non_existent_node_raises_exception(self):    
        self.assertRaises(ValueError, TextNode, "This is a text", TextType.ERROR)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
        
        
if __name__ == "__main__":
    unittest.main()