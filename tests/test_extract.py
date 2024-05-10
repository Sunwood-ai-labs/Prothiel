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
            self.assertEqual(content, 'print("Hello, World!")')

        with open('test_output/folder/file2.py', 'r') as file:
            content = file.read()
            self.assertEqual(content, 'def greet(name):\n    print(f"Hello, {name}!")')

if __name__ == '__main__':
    unittest.main()