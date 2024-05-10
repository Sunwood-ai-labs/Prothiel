from setuptools import setup, find_packages

setup(
    name='prothiel',
    version='0.1.0',
    description='A package to extract code blocks from markdown and organize them into Python files',
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
)