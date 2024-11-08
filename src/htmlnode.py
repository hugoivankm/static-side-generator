
class HTMLNode:
    """
    A class that represents an HTML node 
    
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        __error = self.__validate_HTML_node()
        if __error != "":
            raise AttributeError(__error)
        
    def __repr__(self) -> str:
       return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
   
    def __eq__(self, other: object) -> bool:
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
       
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f'{k}="{v}"' for k, v in self.props.items()])
      

    def __validate_HTML_node(self):

        if self.tag is not None:
            return ""
        
        elif self.tag is None and self.value is not None:
            return ""
        
        elif self.value is None and self.children is not None:
            return ""

        elif self.children is None and self.value is not None:
            return ""
        
        elif self.props is None and self.value is not None:
            return ""
        else:
            return "Invalid HTML node parameters"
        
        
