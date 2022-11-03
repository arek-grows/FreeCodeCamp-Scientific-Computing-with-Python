def test_func(a: int, b: str):
    apd = f"{str(a)}{b}"
    return apd


print(test_func.__doc__)
