from src.textnode import TextType, TextNode
import re


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

    @staticmethod
    def extract_markdown_images(self, text):
        '''
        Example:
        Input:
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        Output:
        [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        '''
        result = []
        matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        for match in matches:
            result.append((match[0], match[1]))
        return result
            
               
    @staticmethod
    def extract_markdown_links(self, text):

        '''
        Example:
        Input:
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        
        Output:
        [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        '''
        result = []
        matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        for match in matches:
            result.append((match[0], match[1]))
        return result

    
    #     node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_link([node])
    # [
    #     TextNode("This is text with a link ", TextType.TEXT),
    #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]
    
    @staticmethod
    def split_nodes_image(self, old_nodes):
        raise NotImplementedError("Not implemented")
   
   
    @staticmethod
    def split_nodes_link(self, old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            original_text = text = old_node.text
            original_text_type = old_node.text_type
            
            links = MarkdownParser.extract_markdown_links(self, original_text)
            for link in links:
               link_text = link[0]
               link_url = link[1]
               last_link = links[-1]
                
               sections = text.split(f"[{link_text}]({link_url})")
               previous_non_link = sections[0]
               rest_of_text = ""
               
               if len(sections) == 2:
                   rest_of_text = sections[1]
                
               if previous_non_link:
                   new_nodes.append(TextNode(sections[0], original_text_type))
               new_nodes.append(TextNode(link_text, TextType.LINK ,f"{link_url}"))
               
               if rest_of_text and (link is last_link):
                   new_nodes.append(TextNode(rest_of_text, original_text_type))
               
               text = rest_of_text
        return new_nodes
               
            
               