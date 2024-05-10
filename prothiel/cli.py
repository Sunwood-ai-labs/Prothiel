import argparse
from .extract import extract_code_blocks

def main():
    parser = argparse.ArgumentParser(description='Extract code blocks from markdown and organize them into Python files.')
    parser.add_argument('markdown_file', help='Path to the markdown file')
    parser.add_argument('root_path', help='Root path for the extracted files')
    parser.add_argument('--file-path-pattern', default=r'### (.*?)\n', help='Regex pattern for file paths')
    parser.add_argument('--code-block-pattern', default=r'```python\n(.*?)\n```', help='Regex pattern for code blocks')
    args = parser.parse_args()

    with open(args.markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    extract_code_blocks(markdown_content, args.root_path, args.file_path_pattern, args.code_block_pattern)