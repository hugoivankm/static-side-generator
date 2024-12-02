from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode, HTMLNode
from textnode import TextNode
from leafnode import LeafNode
from markdown_parser import MarkdownParser
from typing import Pattern
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
    def block_to_block_type(markdown_block: str):
        block_re_dict = {
            BlockType.HEADING: (r"^#{1,6} (.+)", 'single'),
            BlockType.CODE: (r"```(?:[^```]+|`(?!``)|``(?!`))*```", 'single'),
            BlockType.QUOTE: (r"^>(.*?)", 'single'),
            BlockType.UNORDERED_LIST: (r"^(\*|-) (.*)$", 'multi'),
            BlockType.ORDEREDLIST: (r"^\d+.\s(.+)$", 'multi'),
        }

        # pattern is a BlockType
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

    @staticmethod
    def markdown_to_blocks(markdown: str) -> list[str]:
        lines = [line.strip() for line in markdown.splitlines()]
        markdown = "\n".join(lines).strip()
        split_lines = markdown.split("\n\n")
        return split_lines

    @staticmethod
    def _strip_block(block: list[str]):
        lines = block.split("\n")
        filtered = filter(lambda line: line.strip() != '', lines)
        return "\n".join(map(lambda line: line.strip(), filtered))

    @staticmethod
    def markdown_to_html_node(markdown: str) -> ParentNode:
        block_strings = Block.markdown_to_blocks(markdown)
        children = []
        for block_string in block_strings:
            html_node = Block.text_to_child(block_string)
            children.append(html_node)   
        return ParentNode('div', children)
    
    @staticmethod
    def text_to_child(text: str) -> HTMLNode:
        '''
        Takes the text of a markdown block and retuns the respective HTMLNode 
        '''
        block_type = Block.block_to_block_type(text)
        html_node: HTMLNode = None
        match block_type:
            case 'heading':
                heading_type = Block._parse_heading_type_from_text(text)
                text = Block._strip_sequence(text, r'#{1,6} ')
                children = Block._text_to_HTMLNode_list(text)
                html_node = ParentNode(heading_type, children)
            case 'code':
                text = Block._strip_sequence(text, r"```\s*|\s*```")
                children = [LeafNode('code', text)]
                html_node = ParentNode('pre', children)
            case 'quote':
                text = text.strip()
                text = Block._strip_sequence(text, r'> ')
                children = Block._text_to_HTMLNode_list(text)
                html_node = ParentNode("blockquote", children)
            case 'unordered list':
                text = Block._strip_sequence(text, r"\* ")
                children = Block._parse_list_items(text)
                html_node = ParentNode('ul', children)
            case 'ordered list':
                text = Block._strip_sequence(text, r"\d+\.\s+")
                children = Block._parse_list_items(text)
                html_node = ParentNode('ol', children)
            case 'paragraph':
                children = Block._text_to_HTMLNode_list(text)
                html_node = ParentNode('p', children)
            case _:
                raise ValueError("Block is not supported")
        return html_node

    @staticmethod
    def _text_to_HTMLNode_list(text) -> list[HTMLNode]:
        text_nodes = MarkdownParser.text_to_text_nodes(text)
        mapped_html_nodes = map(
            lambda node: TextNode.text_node_to_html_node(node), text_nodes)
        return list(mapped_html_nodes)

    @staticmethod
    def _parse_heading_type_from_text(heading_text: str) -> str:
        regex = re.match(r"^#{1,6}", heading_text)
        if not regex:
            raise ValueError("Value is not a headring")
        span = regex.span()
        return f"h{(span[1] - span[0])}"

    @staticmethod
    def _parse_list_items(items: str) -> list[ParentNode]:
        if not items.strip():
            raise ValueError("items parameter must have a non empty value")
        li_list = []
        list_items: list[str] = items.split("\n")
        for item in list_items:
            li_list.append(ParentNode(
                'li', children=Block._text_to_HTMLNode_list(item)))
        return li_list

    @staticmethod
    def _strip_sequence(text: str, pattern: Pattern[str]) -> str:
        compiled_pattern = re.compile(pattern)
        return re.sub(compiled_pattern, "", text)
