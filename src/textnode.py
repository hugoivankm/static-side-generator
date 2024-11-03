from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    """
    A class representing Text Node for as an intermidiate representation from markdown to HTML
    
    Attributes:
        text - The text content of the node
        text_type - The type of text this node contains, which is a member of the TextType enum. You'll have to get the .value from the enum value you pass in.
        url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    """
    __Sentinel = object()
    def __init__(self, text, text_type, url=__Sentinel) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
        
        valid_text_types = TextNode.__get_valid_text_nodes_type()
        
        if not hasattr(self.text_type, 'value') or (self.text_type.value not in valid_text_types):
             raise ValueError("type not in text types")                
    
    def __eq__(self, other: object) -> bool:
        return (
            self.text == other.text and 
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        if self.url == TextNode.__Sentinel:
            return f"TextNode({self.text}, {self.text_type.value})"            
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    @classmethod
    def print_text_types(cls):
        for type in TextType:
            print(type.value)
    
    @classmethod
    def __get_valid_text_nodes_type(cls):
        valid_text_nodes_type = []
        for type in TextType:
            valid_text_nodes_type.append(type.value)
        return valid_text_nodes_type