def fizzbuzz_v1(start: int, end: int) -> None:
    for num in range(start, end+1):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

def fizzbuzz_v2(start: int, end: int) -> None:
    for number in range(start, end+1):
        result = ''
        result = "Fizz" if number % 3 == 0 else result
        result = f"{result}Buzz" if number % 5 == 0 else result
        print(number if result == '' else result)

fizzbuzz_v2(1,15)