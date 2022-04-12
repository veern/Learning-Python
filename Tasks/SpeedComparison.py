import time

def palindrome_v1(strng: str) -> bool:
    return strng == strng[::-1]

def palindrome_v2(strng: str) -> bool:
    for x in range(len(strng)):
        if strng[x] != strng[-x]:
            return False
    
    return True

t1 = time.time()
for _ in range(1000001):
    palindrome_v1("kayak")
t2 = time.time()
print(f".v1 took: {t2-t1:.5f} seconds")


t1 = time.time()
for _ in range(1000001):
    palindrome_v2("kayak")
t2 = time.time()
print(f".v2 took: {t2-t1:.5f} seconds")

#Less Python == faster