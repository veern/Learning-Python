import time
import logging

"""Program is responsible for finding primes up to a given number while using generators"""

logging.basicConfig(level=logging.DEBUG, 
                    filename="logtext.log", 
                    filemode="w",
                    encoding="utf-8")


def prime_check(number: int) -> bool:
    for divisor in range(2, int(number**0.5)+1):
        if number % divisor == 0:
            return False
    logging.debug(f"Found prime: {number}")
    return True
                    
def Prime_generator(max: int) -> int:
    i = 2
    while i <= max:
        if prime_check(i):
            yield i
        i += 1

NUMBER = 50 

primes = Prime_generator(NUMBER)
for prime in primes:
    print(prime)