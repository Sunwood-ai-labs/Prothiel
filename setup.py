from setuptools import setup, find_packages

# READMEファイルの内容を読み込む
with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()

setup(
    name='prothiel',
    version='0.1.1',
    # PyPIに表示される長い説明文
    long_description=long_description,
    # 長い説明文のフォーマット
    long_description_content_type="text/markdown",
    # プロジェクトのURL
    url="https://github.com/Sunwood-ai-labs/Prothiel",
    author='Maki',
    author_email='sunwood.ai.labs@gmail.com',
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
    # パッケージの分類情報
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
)