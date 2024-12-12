import unittest
import sys
import os

# Add the `src` directory to the sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_can_create_h1(self):
        try:
            node = HTMLNode("h1", "heading test")
        except Exception as e:
            self.fail(f"Object creation failed with exception: {e}")
        self.assertIsInstance(node, HTMLNode)

    def test_can_create_anchor_tag(self):
        try:
            node = HTMLNode(
                "a",
                "anchor test",
                props='{ "href": "https://www.google.com", "target": "_blank",}',
            )
        except Exception as e:
            self.fail(f"HTML node creation failed with exception: {e}")
        self.assertIsInstance(node, HTMLNode)

    def test_can_create_raw_text(self):
        try:
            node = HTMLNode(value="Raw Text test")
        except Exception as e:
            self.fail(f"HTML node creation failed with exception: {e}")
        self.assertIsInstance(node, HTMLNode)

    def test_no_arguments_raises_exception(self):
        self.assertRaises(AttributeError, HTMLNode)


if __name__ == "__main__":
    unittest.main()
