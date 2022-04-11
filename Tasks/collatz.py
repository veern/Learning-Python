def collatz(starting_number: int) -> int:
    """This function returns number of steps it took to reach 1 using the Collatz conjecture"""
    if starting_number < 1: 
        return "Collatz conjecture requires you to start with a number bigger than 1."
    num, steps = starting_number, 0
    while starting_number != 1:
        if starting_number % 2 == 1:
            starting_number = starting_number * 3 + 1
        else:
            starting_number = starting_number / 2
        steps += 1
    print(f"It took {steps} steps for {num} to reach 1.")
    return steps

collatz(8321)