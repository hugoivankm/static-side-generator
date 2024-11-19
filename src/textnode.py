from enum import Enum
from src.leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """
    A class representing Text Node as an intermidiate representation from markdown to HTML

    Attributes:
        text - The text content of the node
        text_type - The type of text this node contains, which is a member of the TextType enum. You'll have to get the .value from the enum value you pass in.
        url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    """
    __Sentinel = object()

    def __init__(self, text: str, text_type: TextType, url=__Sentinel) -> None:
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
            return f'TextNode("{self.text}", {self.text_type})'
        return f'TextNode("{self.text}", {self.text_type}, {self.url})'

    def text_node_to_html_node(self):
        text_type = self.text_type
        if text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if text_type == TextType.LINK:
            return LeafNode("a", self.text, {'href': self.url})
        if text_type == TextType.IMAGE:
            return LeafNode("img", "", {'alt': self.text,  'src': self.url})
        raise ValueError("Text type must be a valid value")

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
