
<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/Prothiel/main/docs/Prothiel_icon.png" width="100%">
<br>
<h1 align="center">Prothiel</h1>
<h2 align="center">
  ～AI Harmony, Infinite Possibilities～

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MakiAi/Prothiel)
[![Prothiel - Sunwood-ai-labs](https://img.shields.io/static/v1?label=Prothiel&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/Sunwood-ai-labs/Prothiel "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/Sunwood-ai-labs/Prothiel?style=social)](https://github.com/Sunwood-ai-labs/Prothiel)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/Sunwood-ai-labs/Prothiel?style=social)](https://github.com/Sunwood-ai-labs/Prothiel)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/Prothiel)](https://github.com/Sunwood-ai-labs/Prothiel)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/Prothiel)](https://github.com/Sunwood-ai-labs/Prothiel)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/Prothiel?sort=date&color=red)](https://github.com/Sunwood-ai-labs/Prothiel)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/Prothiel?color=orange)](https://github.com/Sunwood-ai-labs/Prothiel)

  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。


## 🌟 はじめに

Prothielは、Markdownファイルからコードブロックを抽出し、それらを構造化されたファイル階層に整理するプロセスを簡素化する強力なPythonパッケージです。Prothielを使用すると、Markdownドキュメントを実行可能なPythonコードに簡単に変換できるため、開発者やテクニカルライターにとって貴重なツールとなります。

## ✨ 特徴

- 🔍 カスタマイズ可能なパターンに基づいてMarkdownファイルからコードブロックを抽出
- 📂 抽出されたコードをクリーンなファイル構造に整理
- 🎨 可読性を向上させるためのシンタックスハイライトをサポート 
- 🧪 コードの整合性を確保するための組み込みテスト機能
- 🚀 ワークフローにシームレスに統合するためのコマンドラインインターフェイスを提供

## 🚀 始め方

### 前提条件

- Python 3.11以降

### インストール

1. 新しいconda環境を作成します:
   ```
   conda create -n prothiel python=3.11
   ```

2. 環境をアクティベートします:
   ```
   conda activate prothiel
   ```

3. Prothielをインストールします:
   ```
   pip install prothiel
   ```

### 使用方法

1. 次の形式でコードブロックを含むMarkdownファイルを用意します:
   ```markdown
   ### path/to/file.py
   ​```python
   # ここにコードを書く
   ​```
   ```

2. コマンドラインからProthielを実行します:
   ```
   prothiel path/to/markdown_file.md output_directory
   ```

   Prothielは、Markdownファイルからコードブロックを抽出し、指定された出力ディレクトリに対応するPythonファイルを作成します。

### 例

次の内容を持つ`example.md`というMarkdownファイルがあるとします:

```markdown
# Math functions

## Description

このテンプレートには、簡単な計算機能を持つ4つのPythonファイルが含まれています。各ファイルは基本的な算術演算を行う関数を定義しています。

### math_functions/basic_math/addition.py
​```python
def add(a, b):
    return a + b
​```

### math_functions/basic_math/subtraction.py
​```python
def subtract(a, b):
    return a - b
​```

## 発展的な数学

### math_functions/advanced_math/multiplication.py
​```python  
def multiply(a, b):
    return a * b
​```

### math_functions/advanced_math/division.py
​```python
def divide(a, b):
    if b != 0:  
        return a / b
    else:
        raise ValueError("0での除算は許可されていません。")
​```
```

コードブロックを抽出してPythonファイルに整理するには、次のコマンドを実行します:

```
prothiel --markdown_file=example/01_math_functions.md --root_path=example/01_math_functions
prothiel --markdown_file=example/02_Project_Example.md --root_path=example/02_Project_Example
```

Prothielは次のファイル構造を作成します:

```
math_functions/
├── basic_math/
│   ├── addition.py
│   └── subtraction.py
└── advanced_math/
    ├── multiplication.py
    └── division.py
```

## 📚 ドキュメント

詳細なドキュメントと高度な使用法については、[Prothielドキュメント](https://prothiel.readthedocs.io)を参照してください。

## 🤝 貢献

貢献は大歓迎です！アイデア、提案、バグ報告がある場合は、Issueを開くかプルリクエストを送ってください。詳細については[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

## 📄 ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下でライセンスされています。

## 🙏 謝辞

オープンソースコミュニティの皆様の貴重な貢献と着想に感謝いたします。

---

Prothielを使って、Markdownファイルからのコード抽出を楽々と始めましょう！🚀✨