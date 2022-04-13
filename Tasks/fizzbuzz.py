def fizzbuzz(start: int, end: int) -> None:
    for num in range(start, end+1):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            print(num)

fizzbuzz(1, 15)