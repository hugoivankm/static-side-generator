from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props=None) -> None:
        if value is None:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        if self.props is None or not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>" 
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode(tag="{self.tag}", value="{self.value}", props="{self.props}")'
    
    
    def __eq__(self, other: object) -> bool:
        return super().__eq__(other)


      