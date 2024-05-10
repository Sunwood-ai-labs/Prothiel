import argparse
from .extract import extract_code_blocks
from .run_tests import run_tests
import os
from art import *
import prothiel
import sys

def main():
    parser = argparse.ArgumentParser(description='MarkdownファイルからコードブロックをPythonファイルとして抽出・整理します。')
    parser.add_argument('--markdown_file', default='.Prothiel.md', help='読み込むMarkdownファイルのパス')
    parser.add_argument('--root_path', default='./', help='抽出したファイルを保存するルートパス')
    parser.add_argument('--file-path-pattern', default=r'### (.*?)\n', help='ファイルパスを抽出するための正規表現パターン')
    parser.add_argument('--code-block-pattern', default=r'```python\n(.*?)\n```', help='コードブロックを抽出するための正規表現パターン')
    args = parser.parse_args()
    
    tprint("Prothiel - v{:}".format(str(prothiel.__version__)))
    
    sys.path.append(args.root_path)

    with open(args.markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    extract_code_blocks(markdown_content, args.root_path, args.file_path_pattern, args.code_block_pattern)
    run_tests(args.root_path)
    
    tprint("!! successfully !!")