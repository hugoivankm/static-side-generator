import unittest

from textnode import TextNode, TextType

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
        
if __name__ == "__main__":
    unittest.main()