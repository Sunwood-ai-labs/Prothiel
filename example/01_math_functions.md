# Title

## Description

このテンプレートには、簡単な計算機能を持つ4つのPythonファイルが含まれています。各ファイルは基本的な算術演算を行う関数を定義しています。

## File Structure

- math_functions/
  - basic_math/
    - addition.py
    - subtraction.py
  - advanced_math/
    - multiplication.py
    - division.py

## Source Code

### math_functions/basic_math/addition.py

```python
def add(a, b):
    return a + b
```

### math_functions/basic_math/subtraction.py

```python
def subtract(a, b):
    return a - b
```

### math_functions/advanced_math/multiplication.py

```python
def multiply(a, b):
    return a * b
```

### math_functions/advanced_math/division.py

```python
def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")
```