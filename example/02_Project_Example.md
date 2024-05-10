# Python Project Example

## Description

このプロジェクトは、簡単な計算機能を持つPythonスクリプトの例です。四則演算（足し算、引き算、掛け算、割り算）や素数判定、階乗計算などの機能を提供します。

## File Structure

```
- calculator/
  - math_ops.py
  - number_theory.py
- utils/
  - helpers.py
  - validators.py
- tests/
  - test_math_ops.py
  - test_number_theory.py
```

## Source Code

### calculator/math_ops.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero!")
```

### calculator/number_theory.py

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### utils/helpers.py

```python
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)
```

### utils/validators.py

```python
def validate_integer(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} is not an integer")

def validate_positive(n):
    if n < 0:
        raise ValueError(f"{n} is not a positive number")
```

## Test Cases

### tests/test_math_ops.py

```python
import unittest
from calculator.math_ops import add, subtract, multiply, divide

class TestMathOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
```

### tests/test_number_theory.py

```python
import unittest
from calculator.number_theory import is_prime, factorial

class TestNumberTheory(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0)) 
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
```

このようなプロジェクト構成とソースコード、テストケースを作成しました。基本的な計算機能を提供し、テストケースでその機能を検証しています。バリデーションやエラーハンドリングも一部取り入れています。