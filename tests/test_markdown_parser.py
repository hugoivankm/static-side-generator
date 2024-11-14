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


if __name__ == "__main__":
    unittest.main()
