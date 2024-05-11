import argparse
from .extract import extract_code_blocks
from .run_tests import run_tests
import os
from art import *
import prothiel
import sys
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description='MarkdownファイルからコードブロックをPythonファイルとして抽出・整理します。')
    parser.add_argument('--markdown_file', default='.Prothiel.md', help='読み込むMarkdownファイルのパス')
    parser.add_argument('--root_path', default='./', help='抽出したファイルを保存するルートパス')
    parser.add_argument('--file-path-pattern', default=r'### (.*?)\n', help='ファイルパスを抽出するための正規表現パターン')
    parser.add_argument('--code-block-pattern', default=r'```(python|markdown)\n(.*?)\n```', help='コードブロックを抽出するための正規表現パターン')
    args = parser.parse_args()
    
    tprint("Prothiel - v{:}".format(str(prothiel.__version__)))
    
    sys.path.append(args.root_path)

    # 指定されたMarkdownファイルが存在するかチェック
    if not os.path.exists(args.markdown_file):
        # ファイルが存在しない場合は空のファイルを作成して終了
        with open(args.markdown_file, 'w') as file:
            pass
        print(colored("-"*50, 'red'))
        print(colored(f"指定されたMarkdownファイル '{args.markdown_file}' が存在しないため\n空のファイルを作成しました。", 'red'))
        print(colored("-"*50, 'red'))
        return

    with open(args.markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Markdownファイルが空の場合は終了
    if not markdown_content.strip():
        print(colored("-"*50, 'red'))
        print(colored(f"指定されたMarkdownファイル '{args.markdown_file}' が空です。", 'red'))
        print(colored("-"*50, 'red'))
        return

    extract_code_blocks(markdown_content, args.root_path, args.file_path_pattern, args.code_block_pattern)
    run_tests(args.root_path)
    
    tprint("!! successfully !!")