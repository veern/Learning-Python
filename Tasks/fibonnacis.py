def fibonnaci_iter_gen(num: int) -> int:
    """Fibonnaci function yields a value that is smaller that given num"""
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a + b

def fibonnaci_iter(num: int) -> int:
    """Fibonnaci function that returns a value at a specific index"""
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a

def fibonnaci_rec(num: int) -> int:
    """Recursive Fibonnaci function that returns a value at a specific index"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonnaci_rec(num - 2) + fibonnaci_rec(num - 1)

fib_iter = []

for number in fibonnaci_iter_gen(100):
    fib_iter.append(number)

fib_iter_2 = fibonnaci_iter(5)

fib_rec = fibonnaci_rec(5)

print(f"Iteracyjna wersja ciągu fibonnaciego: {fib_iter}")
print(f"Iteracyjna wersja ciągu fibonnaciego: {fib_iter_2}")
print(f"Rekursywna wersja ciągu fibonnaciego: {fib_rec}")
