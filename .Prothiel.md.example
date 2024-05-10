# Prothiel

## Description

Prothiel is a Python package that extracts file paths and code blocks from a markdown file, organizes the code into separate Python files, and runs test cases for the extracted code. It supports nested code blocks and can be executed from the command line with configurable options.

## File Structure

```
- prothiel/
  - __init__.py
  - extract.py
  - utils.py
  - cli.py
- tests/
  - test_extract.py
- setup.py
- README.md
```

## Source Code

### prothiel/\_\_init\_\_.py

```python
from .extract import extract_code_blocks
```

### prothiel/extract.py

```python
import re
import os
from termcolor import colored
from .utils import create_directory, write_file

def extract_code_blocks(markdown_content, root_path, file_path_pattern, code_block_pattern):
    file_path_matches = re.finditer(file_path_pattern, markdown_content)

    for file_path_match in file_path_matches:
        file_path = file_path_match.group(1).strip()
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
```

### prothiel/utils.py

```python
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
```

### prothiel/cli.py

```python
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
```

### setup.py

```python
from setuptools import setup, find_packages

setup(
    name='prothiel',
    version='0.2.0',
    description='A package to extract code blocks from markdown and organize them into Python files',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'termcolor',
        'art',
    ],
    entry_points={
        'console_scripts': [
            'prothiel=prothiel.cli:main',
        ],
    },
)
```

## Test Cases

### tests/test_extract.py

```python
import unittest
from prothiel.extract import extract_code_blocks

class TestExtract(unittest.TestCase):
    def test_extract_code_blocks(self):
        markdown_content = '''
### file1.py
```python
print("Hello, World!")
```

### folder/file2.py
```python
def greet(name):
    print(f"Hello, {name}!")
```
'''
        root_path = 'test_output'
        file_path_pattern = r'### (.*?)\n'
        code_block_pattern = r'```python\n(.*?)\n```'
        extract_code_blocks(markdown_content, root_path, file_path_pattern, code_block_pattern)

        with open('test_output/file1.py', 'r') as file:
            content = file.read()
            self.assertEqual(content, 'print("Hello, World!")\n')

        with open('test_output/folder/file2.py', 'r') as file:
            content = file.read()
            self.assertEqual(content, 'def greet(name):\n    print(f"Hello, {name}!")\n')

if __name__ == '__main__':
    unittest.main()
```