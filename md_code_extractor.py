import re
import os
import unittest
from termcolor import colored
from art import *
import shutil
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

script_name = os.path.basename(__file__)
tprint(script_name)

# ルートパスを設定
root_path = "./"

sys.path.append(root_path)

# マークダウンファイルを読み込む
markdown_path = "tmp.md"

with open(markdown_path, 'r', encoding="utf8") as file:
    markdown_content = file.read()

# ファイルパスとコードブロックを抽出するための正規表現パターン
pattern = r'### (.*?)\n```python\n(.*?)\n```'

# ファイルパスとコードブロックを抽出
matches = re.findall(pattern, markdown_content, re.DOTALL)

# # 抽出した情報を整理して出力
# for file_path, code_block in matches:
#     file_path = file_path.strip()  # ファイルパスから改行文字を取り除く
    
#     print(colored(f"File path: {file_path}", 'blue'))
#     print(colored("Code block:", 'green'))
#     print(colored(code_block, 'yellow'))
#     print()

#     # ファイルパスをルートパスからの相対パスに変更
#     file_path = os.path.join(root_path, file_path)

#     # ファイルパスのディレクトリが存在しない場合は作成
#     directory = os.path.dirname(file_path)
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     # ファイルにコードブロックの内容を書き込む
#     with open(file_path, 'w') as file:
#         file.write(code_block)

# README.mdファイルをルートパスにコピー
shutil.copy(markdown_path, os.path.join(root_path, "README.md"))

# テストケースを順番に実行
test_files = [
    "tests/test_extract.py",
]

for test_file in test_files:
    test_file_path = os.path.join(root_path, test_file)
    print(colored(f"Running tests from: {test_file}", 'magenta'))
    test_suite = unittest.TestLoader().discover(os.path.dirname(test_file_path), os.path.basename(test_file_path))
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    print()