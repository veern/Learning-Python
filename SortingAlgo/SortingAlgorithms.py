def check_for_zero_or_one_len(lst: list) -> bool:
    if lst == [] or len(lst) == 1:
        return True


def check_all_elements(lst: list) -> None:
    if all(isinstance(x, complex) for x in lst):
        raise TypeError("Complex sorting is not implemented")
    elif not all(isinstance(x, (int, float)) for x in lst) or not lst:
        raise TypeError("Not all values in the passed list are integers or floats")


def bubble_sort(lst: list[int]) -> list[int]:
    """
    Bubble sort goes over the list and compares pairs of numbers. 
    After each iteration, it is certain that last number is sorted, so we can shorten the list to iterate.
    """
    if check_for_zero_or_one_len(lst): return lst
    check_all_elements(lst)

    n = len(lst)
    no_swap = True
    for _ in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                no_swap = False
        # If no swap was done during the iteration of a list, then it is already sorted and further iteration is not needed
        if no_swap:
            return lst
        n -= 1
    return lst


def insert_sort(lst: list[int]) -> list[int]:
    """
    Insert sort goes over the list of numbers once and each time a number on the right is bigger than
    the one on the left, function iterates backwards to find its correct spot, shifting all elements to the right
    """
    if check_for_zero_or_one_len(lst):
        return lst
    check_all_elements(lst)
    
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
    if check_for_zero_or_one_len(lst): return lst
    check_all_elements(lst)
    
    n = 0
    for i in range(len(lst)):
        current_minimum = i
        for j in range(n, len(lst)):
            if lst[current_minimum] > lst[j]:
                current_minimum = j
        if current_minimum != i:  # if no new current_minimum was found, then the swap is not needed
            lst[i], lst[current_minimum] = lst[current_minimum], lst[i]
        n += 1
    return lst
