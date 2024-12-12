import unittest
import sys
import os

# Add the `src` directory to the sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_can_create__p_with_leaf_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(actual, expected)

    def test_can_create_p_with_parent_nodes(self):
        nested_parent_1 = ParentNode(
            "i",
            [
                LeafNode("b", "text"),
                LeafNode(None, "Normal text"),
            ],
        )

        nested_parent_2 = ParentNode(
            "b",
            [
                LeafNode(None, "More Normal text "),
                LeafNode("a", "This is a link", {"href": "example.com"}),
            ],
        )

        node = ParentNode("p", [nested_parent_1, nested_parent_2])

        actual = node.to_html()
        expected = '<p><i><b>text</b>Normal text</i><b>More Normal text <a href="example.com">This is a link</a></b></p>'

        self.assertEqual(actual, expected)

    def test_can_create_p_with_parent_and_leaf_nodes(self):
        nested_leaf_1 = LeafNode("h3", "Section title")
        nested_parent_1 = ParentNode(
            "i",
            [
                LeafNode("b", "text"),
                LeafNode(None, "Normal text"),
            ],
        )

        nested_parent_2 = ParentNode(
            "b",
            [
                LeafNode(None, "More Normal text "),
                LeafNode("a", "This is a link", {"href": "example.com"}),
            ],
        )

        node = ParentNode("p", [nested_leaf_1, nested_parent_1, nested_parent_2])

        actual = node.to_html()
        expected = '<p><h3>Section title</h3><i><b>text</b>Normal text</i><b>More Normal text <a href="example.com">This is a link</a></b></p>'

        self.assertEqual(actual, expected)

    def test_parent_with_children_raises_exception(self):
        self.assertRaises(ValueError, ParentNode, "p", [])

    def test_parent_with_no_tag_raises_exception(self):
        self.assertRaises(
            ValueError,
            ParentNode,
            None,
            [
                LeafNode(None, "More Normal text "),
                LeafNode("a", "This is a link", {"href": "example.com"}),
            ],
        )
