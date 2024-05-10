def validate_integer(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} is not an integer")

def validate_positive(n):
    if n < 0:
        raise ValueError(f"{n} is not a positive number")