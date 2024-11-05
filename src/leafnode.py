from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        if not value:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        if self.props is None or not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"