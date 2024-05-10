import re
import os
from termcolor import colored
from .utils import create_directory, write_file

def extract_code_blocks(markdown_content, root_path, file_path_pattern, code_block_pattern):
    file_path_matches = re.finditer(file_path_pattern, markdown_content)

    for file_path_match in file_path_matches:
        file_path = file_path_match.group(1).strip().replace("\_", "_")
        start_index = file_path_match.end()

        code_block_match = re.search(code_block_pattern, markdown_content[start_index:], re.DOTALL)
        if code_block_match:
            code_block = code_block_match.group(1)
            print(colored(f"File path: {file_path}", 'blue'))
            print(colored("Code block:", 'green'))
            print(colored(code_block, 'yellow'))
            print()

            file_path = os.path.join(root_path, file_path)
            directory = os.path.dirname(file_path)
            create_directory(directory)
            write_file(file_path, code_block)