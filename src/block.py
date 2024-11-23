from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDEREDLIST = "ordered_list"
    

class Block:
    """
    A class representing Block Node that has markdown content and a block type

    Attributes:
        content - Markdown content for the block
        block_type - The type of content this block node contains, which is a member of the Block enum.
    """
    def __init__(self, content: str, block_type: BlockType) -> None:
        if not content:
            raise ValueError("Block node must have markdown content")
        
        self.content = content
        self.block_type = block_type
        
    def __repr__(self) -> str:
        return f'Block("{self.content}", "{self.block_type}")'
    
    def __eq__(self, other):
        return self.content == other.content and self.block_type == other.block_type
    

        
        
        

        
        
        
        