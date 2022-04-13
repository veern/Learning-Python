class Calculator:

    def __init__(self) -> None:
        self.signs = ["+", "-", "*", "/", "^"]

    @staticmethod
    def add(num1: int | float, num2: int | float) -> int | float:
        return num1 + num2
    
    @staticmethod
    def subtraction(num1: int | float, num2: int | float) -> int | float:
        return num1 - num2

    @staticmethod
    def multiplication(num1: int | float, num2: int | float) -> int | float:
        return num1*num2

    @staticmethod
    def division(num1: int | float, num2: int | float) -> float:
        return num1/num2

    @staticmethod
    def raise_to_power(num1: int | float, power: int | float) -> int | float:
        return num1**power

    def evaluate(self, strng: str) -> int | float:

        for character in strng:
            if character in self.signs:
                operator = character

        num1, num2 = map(int, strng.split(operator))

        operators = {
            "+": Calculator.add(num1, num2),
            "-": Calculator.subtraction(num1, num2),
            "*": Calculator.multiplication(num1, num2),
            "/": Calculator.division(num1, num2),
            "^": Calculator.raise_to_power(num1, num2),
        }

        return operators[operator]