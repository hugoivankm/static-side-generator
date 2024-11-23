from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDEREDLIST = "ordered list"


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

    @staticmethod
    def block_to_block_type(markdown_block):
        block_re_dict = {
            BlockType.HEADING: (r"^#{1,6} (.+)", 'single'),
            BlockType.CODE: (r"^```\n?.+\n?```$", 'single'),
            BlockType.QUOTE: (r"^>(.*?)", 'single'),
            BlockType.UNORDERED_LIST: (r"^(\*|-) (.*)$", 'multi'),
            BlockType.ORDEREDLIST: (r"^\d+.\s(.+)$", 'multi'),
        }

        # pattern is a BlockTYpe
        for pattern in block_re_dict:
            regex = block_re_dict[pattern][0]
            multiline = block_re_dict[pattern][1]

            if Block._matches_pattern(regex, markdown_block, multiline):
                return pattern.value
        return BlockType.PARAGRAPH.value

    @staticmethod
    def _matches_pattern(pattern, markdown, multiline):
        if multiline == 'multi':
            return bool(re.match(pattern, markdown, re.MULTILINE))
        else:
            return bool(re.match(pattern, markdown))
