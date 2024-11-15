import unittest

from src.textnode import TextType, TextNode
from src.markdown_parser import MarkdownParser


class TestMarkdownParser(unittest.TestCase):
    def test_with_single_code_element(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self,
                                                           [TextNode(
                                                               "This is text with a `code block` word", TextType.TEXT)],
                                                           '`',
                                                           TextType.CODE
                                                           )

        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)
        self.assertEqual(actual, expected)

    def test_with_node_bold_element_before_code_element(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self, [
            TextNode("**This is a bold title**", TextType.BOLD),
            TextNode("This is text with a `code block` word", TextType.TEXT)],
            '`',
            TextType.CODE
        )

        expected = '[TextNode("**This is a bold title**", TextType.BOLD), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)

        self.assertEqual(actual, expected)

    def test_with_italic_element_after_code_element(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self, [
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("*This is an italic title*", TextType.ITALIC)],
            '`',
            TextType.CODE
        )
        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT), TextNode("*This is an italic title*", TextType.ITALIC),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)

        self.assertEqual(actual, expected)

    def test_exception_raised_for_invalid_markdows(self):
        self.assertRaises(
            ValueError,
            MarkdownParser.split_nodes_delimiter, self,
            [TextNode("This is text with a `code block word", TextType.TEXT)],
            '`',
            TextType.CODE
        )
    def test_extract_markdown_images_should_return_valid_tuple_list(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = MarkdownParser.extract_markdown_images(self, text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        
        self.assertEqual(actual, expected)
        
    def test_extract_markdown_links_should_return_valid_tuple_list(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = MarkdownParser.extract_markdown_links(self, text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
