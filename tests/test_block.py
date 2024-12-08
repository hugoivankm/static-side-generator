import unittest
import sys
import os

# Add the `src` directory to the sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')))

from textnode import TextType, TextNode
from markdown_parser import MarkdownParser
from block import Block, BlockType


class TestBlock(unittest.TestCase):
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

    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual = MarkdownParser.text_to_text_nodes(text)

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

    def test_markdown_to_blocks(self):
        markdown = """# This is a heading
                   
                   This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                   * This is the first list item in a list block
                   * This is a list item
                   * This is another list item
                   
                   1. First Item
                   2. Second Item           
                """
        actual = Block.markdown_to_blocks(markdown)
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item", "1. First Item\n2. Second Item"]

        self.assertEqual(actual, expected)

    def test_markdown_to_html_node_with_heading_paragraph_and_unordered_list(self):
        markdown = """
                   # This is a heading
                   
                   This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                   * This is the first list item in a list block
                   * This is a list item
                   * This is another list item  
                """
        actual = Block.markdown_to_html_node(markdown).__repr__()
        expected = '''ParentNode(tag="div", children="[ParentNode(tag="h1", children="[LeafNode(tag="None", value="This is a heading", props="None")]", props="None"), ParentNode(tag="p", children="[LeafNode(tag="None", value="This is a paragraph of text. It has some ", props="None"), LeafNode(tag="b", value="bold", props="None"), LeafNode(tag="None", value=" and ", props="None"), LeafNode(tag="i", value="italic", props="None"), LeafNode(tag="None", value=" words inside of it.", props="None")]", props="None"), ParentNode(tag="ul", children="[ParentNode(tag="li", children="[LeafNode(tag="None", value="This is the first list item in a list block", props="None")]", props="None"), ParentNode(tag="li", children="[LeafNode(tag="None", value="This is a list item", props="None")]", props="None"), ParentNode(tag="li", children="[LeafNode(tag="None", value="This is another list item", props="None")]", props="None")]", props="None")]", props="None")'''

        self.assertEqual(actual, expected)

    def test_markdown_to_html_node_with_headings_code_and_ordered_list_of_images_and_links(self):
        markdown = """
                   # This is a heading
                   
                   ## This is a different heading
                   
                    ``` 
                    print("hello there")
                    ```
                             
                   1. ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
                   2. [google](google.com)
    
                """

        actual = Block.markdown_to_html_node(markdown).__repr__()
        expected = '''ParentNode(tag="div", children="[ParentNode(tag="h1", children="[LeafNode(tag="None", value="This is a heading", props="None")]", props="None"), ParentNode(tag="h2", children="[LeafNode(tag="None", value="This is a different heading", props="None")]", props="None"), ParentNode(tag="pre", children="[LeafNode(tag="code", value="\nprint("hello there")", props="None")]", props="None"), ParentNode(tag="ol", children="[ParentNode(tag="li", children="[LeafNode(tag="img", value="", props="{'alt': 'obi wan', 'src': 'https://i.imgur.com/fJRm4Vk.jpeg'}")]", props="None"), ParentNode(tag="li", children="[LeafNode(tag="a", value="google", props="{'href': 'google.com'}")]", props="None")]", props="None")]", props="None")'''

        self.assertEqual(actual, expected)
