from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        
    