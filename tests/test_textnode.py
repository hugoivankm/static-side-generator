import unittest
from enum import Enum

from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode


class TextTypeWithError(Enum):
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
        
    def test_text_node_to_html_node_TEXT(self):
        test_text_node = TextNode("This is just text", TextType.TEXT)
        actual = test_text_node.text_node_to_html_node()
        expected = HTMLNode(tag=None,value="This is just text", children=None, props=None)
        self.assertEqual(actual, expected)
        
        test_bold_node = TextNode("This is bold text", TextType.BOLD)   
        actual = test_bold_node.text_node_to_html_node()
        expected = HTMLNode(tag="b",value="This is bold text", children=None, props=None)
        self.assertEqual(actual, expected)
        
        test_link_node = TextNode("This is a link", TextType.LINK, "example.com")   
        actual = test_link_node.text_node_to_html_node()
        expected = HTMLNode(tag="a",value="This is a link", children=None, props={"href":"example.com"})
        self.assertEqual(actual, expected)
        
        test_image_node = TextNode("This is an image", TextType.IMAGE, "example.com")   
        actual = test_image_node.text_node_to_html_node()
        expected = HTMLNode(tag="img",value="", children=None, props={'alt': 'This is an image', 'src': 'example.com'})
        self.assertEqual(actual, expected)
        
    
    def test_non_existent_node_raises_exception(self):    
        self.assertRaises(ValueError, TextNode, "This is a text", TextTypeWithError.ERROR)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
        
        
if __name__ == "__main__":
    unittest.main()