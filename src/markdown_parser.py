from textnode import TextType

class MarkdownParser:
   def __init__(self, text) -> None:
       self.text = text
   
   def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
       new_node = []
       for node in old_nodes:
           if node.text_type == TextType.TEXT:
               sub_list = __parse_string(node.text)
               if self.is_fully_parsed():
                   new_node.extend(sub_list)
               else:
                   self.split_nodes_delimiter(sub_list, delimiter, text_type)                  
           else:
               new_node.extend()
               
               
   def __is__fully_parsed(self, list):
       pass            
   
   def __parse_string(self, target):
       pass