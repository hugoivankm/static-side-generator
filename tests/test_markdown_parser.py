import unittest

from src.textnode import TextType, TextNode
from src.markdown_parser import MarkdownParser


class TestMarkdownParser(unittest.TestCase):
    def test_split__node_delimiter_should_work_with_single_code_element(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self,
                                                           [TextNode(
                                                               "This is text with a `code block` word", TextType.TEXT)],
                                                           '`',
                                                           TextType.CODE
                                                           )

        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)
        self.assertEqual(actual, expected)
    
    def test_split__node_delimiter_should_work_with_previous_pure_text_node(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self,
                                                           [
                                                            TextNode("Hi", TextType.TEXT),
                                                            TextNode(
                                                               "This is text with a `code block` word", TextType.TEXT)],
                                                           '`',
                                                           TextType.CODE
                                                           )

        expected = '[TextNode("Hi", TextType.TEXT), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)
        self.assertEqual(actual, expected)


    def test_split__node_delimiter_should_work_with_node_bold_element_before_code_element(self):
        actual_list = MarkdownParser.split_nodes_delimiter(self, [
            TextNode("**This is a bold title**", TextType.BOLD),
            TextNode("This is text with a `code block` word", TextType.TEXT)],
            '`',
            TextType.CODE
        )

        expected = '[TextNode("**This is a bold title**", TextType.BOLD), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]'
        actual = MarkdownParser.to_node_list_repr(self, actual_list)

        self.assertEqual(actual, expected)

    def test_split__node_delimiter_should_work_with_italic_element_after_code_element(self):
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
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual, expected)

    def test_extract_markdown_links_should_return_valid_tuple_list(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual = MarkdownParser.extract_markdown_links(self, text)
        expected = [("to boot dev", "https://www.boot.dev"),
                    ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual, expected)

    def test_split_nodes_link_should_pass_with_several_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_link(self, [node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        self.assertEqual(actual, expected)

    def test_split_nodes_link_should_pass_with_just_a_link(self):
        node = TextNode(
            "[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_link(self, [node])
        expected = [
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        self.assertEqual(actual, expected)

    def test_split_nodes_link_should_pass_with_just_a_link_and_prepended_text(self):
        node = TextNode(
            "[prepended text](https://www.youtube.com/@bootdotdev)!!!",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_link(self, [node])
        expected = [
            TextNode(
                "prepended text", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("!!!", TextType.TEXT),
        ]

        self.assertEqual(actual, expected)

    def test_split_nodes_image_should_pass_with_several_images(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_image(self, [node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE,
                     "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]

        self.assertEqual(actual, expected)

    def test_split_nodes_image_should_pass_with_a_single_image(self):
        node = TextNode(
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_image(self, [node])
        expected = [
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]

        self.assertEqual(actual, expected)

    def test_split_nodes_image_should_pass_with_prepended_text(self):
        node = TextNode(
            "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)!!!",
            TextType.TEXT,
        )

        actual = MarkdownParser.split_nodes_image(self, [node])
        expected = [
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode("!!!", TextType.TEXT)
        ]

        self.assertEqual(actual, expected)

    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual = MarkdownParser.text_to_text_nodes(self, text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
