from src.textnode import TextType, TextNode


class MarkdownParser:
    @staticmethod
    def split_nodes_delimiter(self, old_nodes: list[TextNode], delimiter: str, text_type: TextType):
        new_node = []
        for node in old_nodes:
            if node.text_type == TextType.TEXT:
                sub_list = MarkdownParser.parse_text_to_node_list(self, node.text, delimiter, text_type)
                new_node = [*new_node, *sub_list]
            else:
                new_node.extend([node])
        return new_node



    @staticmethod
    def parse_text_to_node_list(self, target: str, delimiter: str, text_type: TextType):
        result = target.split(delimiter, 2)
        if len(result) < 3:
            raise ValueError("Invalid Markdown Syntax")
       
        result_list = [
                TextNode(result[0], TextType.TEXT),
                TextNode(result[1], text_type),
                TextNode(result[2], TextType.TEXT),
        ]
        
        return list(filter(lambda item: True if item.text else False, result_list))

    @staticmethod
    def to_node_list_repr(self, list):
        if len(list) < 1:
            return "[]"
        
        representation = ""
        for text_node in list:
             representation += (text_node.__repr__() + ( ", " if text_node != list[-1] else ",")) 
        return f"[{representation}]"