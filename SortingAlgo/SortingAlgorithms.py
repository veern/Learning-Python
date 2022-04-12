def bubble_sort(numlist: list[int]) -> list[int]:
    """
    Bubble sort goes over the list and compares pairs of numbers. 
    After each iteration, it is certain that last number is sorted, so we can shorten the list to iterate.
    """
    N = len(numlist)
    no_swap = True
    for _ in range(N):
        for j in range(N-1):
            if numlist[j] > numlist[j+1]:
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
                no_swap = False
        if no_swap: # If no swap was done during the iteration of a list, then it is already sorted and further iteration is not needed
            return numlist
        N -= 1
    return numlist

def insert_sort(lst: list[int]) -> list[int]:
    """
    Insert sort goes over the list of numbers once and each time a number on the right is bigger than
    the one on the left, function iterates backwards to find its correct spot, shifting all elements to the right
    """
    for i in range(len(lst)):
        j = i
        while lst[j] < lst[j-1] and j > 0:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst

def selection_sort(lst: list[int]) -> list[int]:
    """
    Selection sort iterates over the list, keeping track of a minimum value of each iteration.
    At the end of each iteration, one number is sorted to the correct spot in front of other sorted values.
    Each iteration sorts one number and puts it on the front, first at index 0, then 1 and so on.
    """
    N = 0
    for i in range(len(lst)):
        current_minimum = i
        for j in range(N, len(lst)):
            if lst[current_minimum] > lst[j]:
                current_minimum = j
        if current_minimum != i: # if no new current_minimum was found, then the swap is not needed
            lst[i], lst[current_minimum] = lst[current_minimum], lst[i]
        N += 1
    return lst


# Each array is the same but initialized as different variables. Printing the array to see if it is indeed sorted.
tablica1 = [1,5,4,6,3,7,4,2,7,9,12,13,20, 1, 0,-1]
print("Bubble:", bubble_sort(tablica1))
tablica2 = [1,5,4,6,3,7,4,2,7,9,12,13,20, 1, 0,-1]
print("Insert:", insert_sort(tablica2))
tablica3 = [1,5,4,6,3,7,4,2,7,9,12,13,20, 1, 0,-1]
print("Selection:", selection_sort(tablica3))
