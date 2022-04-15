
def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2

def subtraction(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2

def multiplication(num1: int | float, num2: int | float) -> int | float:
    return num1*num2

def division(num1: int | float, num2: int | float) -> float:
    return num1/num2

def raise_to_power(num1: int | float, power: int | float) -> int | float:
    return num1**power

def evaluate(strng: str) -> int | float:
    signs = ["+", "-", "*", "/", "^"]

    for character in strng:
        if character in signs:
            operator = character

    num1, num2 = map(int, strng.split(operator))

    operators = {
        "+": add(num1, num2),
        "-": subtraction(num1, num2),
        "*": multiplication(num1, num2),
        "/": division(num1, num2),
        "^": raise_to_power(num1, num2),
    }

    return operators[operator]

print(evaluate("643+523"))