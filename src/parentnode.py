from src.htmlnode import HTMLNode
from src.leafnode import LeafNode

class ParentNode(HTMLNode):
    """
    A class representing Parent Node for a represention of HTML
    
    Attributes:
        tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        children - A list of HTMLNode objects representing the children of this node
        props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self, tag, children, props=None) -> None:
        if not tag:
            raise ValueError("All parent nodes must have a tag")
        if not children:
            raise ValueError("All parent nodes must have children")
        super().__init__(tag, None, children, props)
        
    def to_html(self):        
        innerHTML = ""
        for child in self.children:
            if isinstance(child, LeafNode) or isinstance(child, ParentNode):       
                innerHTML += child.to_html()
            else:
                raise ValueError("Invalid Child Property")
        if not self.props:
            return f"<{self.tag}>{innerHTML}</{self.tag}>" 
        return f"<{self.tag} {self.props_to_html()}>{innerHTML}</{self.tag}>" 