import re
import os
from termcolor import colored
from .utils import create_directory, write_file
import pprint
def extract_code_blocks(markdown_content, root_path, file_path_pattern, code_block_pattern):
    code_blocks = {}

    def replace_code_block(match):
        code_block_id = f"__CODE_BLOCK_{len(code_blocks)}__"
        code_blocks[code_block_id] = match.group(0).strip()  # 改行文字を取り除く
        return code_block_id

    # コードブロックを一時的に置換
    markdown_content = re.sub(code_block_pattern, replace_code_block, markdown_content, flags=re.DOTALL)

    file_path_matches = re.finditer(file_path_pattern, markdown_content)
    for file_path_match in file_path_matches:
        file_path = file_path_match.group(1).strip()
        start_index = file_path_match.end()

        next_file_path_match = re.search(file_path_pattern, markdown_content[start_index:])
        if next_file_path_match:
            end_index = start_index + next_file_path_match.start()
        else:
            end_index = len(markdown_content)

        code_block_id = markdown_content[start_index:end_index].strip()

        if code_block_id in code_blocks:
            code_block = code_blocks[code_block_id]
            print(colored(f"File path: {file_path}", 'blue'))
            print(colored(f"---------- Code block [{code_block_id}]: ----------", 'green'))
            print(colored(code_block, 'yellow'))
            
            print()

            file_path = os.path.join(root_path, file_path)
            directory = os.path.dirname(file_path)
            create_directory(directory)

            # コードブロックの言語を判定
            language = re.search(r'```(\w+)', code_block).group(1)
            
            print(colored(f"... language is {language}", 'green'))
            print(colored("---------------------------------", 'green'))
            
            if language == 'python':
                code_content = code_block[code_block.find('\n') + 1:-3].strip()
            elif language == 'markdown':
                code_content = code_block[code_block.find('\n') + 1:-3]
            else:
                code_content = code_block

            write_file(file_path, code_content)
        else:
            print(colored(f"No code block found for file path: {file_path}", 'red'))
            print(colored("Skipping the following content:", 'red'))
            print(colored(markdown_content[start_index:end_index], 'red'))
            print(colored("---------------------------------", 'red'))
            print()