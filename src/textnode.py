from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type, url = None) -> None:
        self.text = text
        self.text_type = TextNode.__get_text_type(text_type)
        self.url = url
    
    def __eq__(self, other: object) -> bool:
        return (
            self.text == other.text and 
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    @classmethod
    def __get_text_type(cls, value: str):
        for type in TextType:
            if value.lower() == type.value:
                return type
        raise ValueError(f"Error: {value} is not a valid text type")

    @classmethod
    def print_text_types(cls):
        for type in TextType:
            print(type.value)