from block import Block
from markdown_parser import MarkdownParser
from typing import Callable
import os
from pathlib import Path, PosixPath


class PathNotFoundError(Exception):
    def __init__(self, path) -> None:
        self.path = path
        self.message = f"The specified path '{
            self.path}' does not exist or additional permissions need to be granted for access"
        super().__init__(self.message)


class UnableToGeneratePage(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


def _replace_pattern(text: str, target: str) -> Callable[[str, str], str]:
    import re

    def replacer(text: str, replacement: str):
        pattern = r"\{\{\s*" + f"{target}" + r"\s*\}\}"
        return re.sub(pattern, replacement, text)

    return replacer


def generate_page(from_path: str, template_path: str, dest_path: str):
    for path_arg in [from_path, template_path, dest_path]:
        if not os.path.exists(path_arg):
            raise PathNotFoundError(path_arg)

    print(
        f"Generating page from {from_path} to {
          dest_path} using {template_path}"
    )

    markdown: str = ""
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    if markdown.strip() == "":
        raise ValueError("markdown file specified in path is empty")

    template: str = ""
    with open(template_path) as template_file:
        template = template_file.read()
    if template.strip() == "":
        raise ValueError("markdown file specified in path is empty")

    content = Block.markdown_to_html_node(markdown).to_html()
    content_replacer = _replace_pattern(template, "Content")
    template = content_replacer(template, content)

    title = MarkdownParser.extract_title(markdown)
    title_replacer = _replace_pattern(template, "Title")
    template = title_replacer(template, title)

    if not os.path.isdir(dest_path):
        raise ValueError("Destination Path must be a valid directory")

    dest_file = os.path.join(dest_path, "index.html")
    with open(dest_file, "w") as dest:
        dest.write(template)


def remove_segment_from_path(
    path: PosixPath, segment_to_remove: str = "content"
) -> PosixPath:
    path_parts: tuple = path.parts
    segment_parts: tuple = PosixPath(segment_to_remove).parts

    # Check if the path starts with the segment to remove
    if path_parts[: len(segment_to_remove.split("/"))] == segment_parts:
        # Join the parts after the segment to remove
        new_path = Path(*path_parts[len(segment_parts) :])
        return new_path
    else:
        # Return the original path if it does not start with the segment to remove
        return path


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
) -> None:
    try:
        for p in Path(dir_path_content).rglob("*"):
            if os.path.isfile(p):
                simplified_path: PosixPath = remove_segment_from_path(p)
                new_dest_dir_path = os.path.join(dest_dir_path, simplified_path.parent)
                if not os.path.exists(new_dest_dir_path):
                    os.makedirs(new_dest_dir_path)
                generate_page(p, template_path, new_dest_dir_path)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        raise UnableToGeneratePage("Unable to generate page")
