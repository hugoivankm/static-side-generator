import unittest
import sys
import os

# Add the `src` directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_can_create_leaf_node_p(self):
        try:
            node = LeafNode(
                'p',
                "p test"
            )
        except Exception as e:
            self.fail(f"Leaf Node creation failed with exception: {e}")
        self.assertIsInstance(node, LeafNode)
        
    def test_can_create_leaf_node_b_none_props(self):
        try:
            node = LeafNode(
                'b',
                "Bold text",
                None
            )
        except Exception as e:
            self.fail(f"Leaf Node creation failed with exception: {e}")
        self.assertIsInstance(node, LeafNode)
        
        
    def test_can_create_leaf_node_anchor(self):
        try:
            node = LeafNode(
            'a',
            "anchor test",
            props='{ "href": "https://www.google.com", "target": "_blank",}')
        except Exception as e:
            self.fail(f"Leaf Node creation failed with exception: {e}")
        
        self.assertIsInstance(node, LeafNode)
        
    def test_leaf_node_p_to_html(self):
        p_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(p_node.to_html(), "<p>This is a paragraph of text.</p>" )
    
    def test_anchor_leaf_node_to_html(self):
        a_node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(a_node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_no_arguments_raises_exception(self):
        self.assertRaises(ValueError, LeafNode, "p", None)
        
        
if __name__ == "__main__":
    unittest.main()