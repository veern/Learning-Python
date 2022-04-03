import string
import itertools
import os

"""
This program checks if a string that consists of letters and question mark could be a palindrome
if question marks were swapped for certain letters. 
For strings with no question marks, it just checks if a string is a palindrome.
"""

def check_if_palindrome(strng: str) -> bool:
    """This function return True or False, depending if given string is a palindrome or not"""
    if len(strng) % 2:
        return strng[:int(len(strng)/2)] == strng[:int(len(strng)/2):-1]
    return strng[:int(len(strng)/2)] ==  strng[:int(len(strng)/2-1):-1]

def find(strng: str, character: str) -> list[int]:
    """This function returns a list of indexes of all occurences of a sign in a string"""
    indexes = [id for id, letter in enumerate(strng) if letter == character]
    return indexes

def replace_question_marks(strng: str) -> list[str]:
    """
    This function returns a list of possible palindromes consisting of a string with question marks.
    Palindromes are created by replacing question marks with any letter. If no question marks, then return empty list.
    """
    if "?" not in strng:
        return [strng] if check_if_palindrome(strng) else []
    palindromes = []
    #If only uppercase or lowercase characters are considered, then change allLetters to their respective string. method.
    allLetters = string.ascii_letters
    questionIndexes = find(strng, "?")
    lstrng = list(strng)
    combinations = itertools.product(allLetters, repeat=len(questionIndexes))
    for combo in combinations:
        for i, questionMark in enumerate(questionIndexes):
            lstrng[questionMark] = combo[i] 
        if check_if_palindrome(lstrng):
            palindromes.append("".join(lstrng))
    return palindromes

def main():
    os.system("cls")
    #For more than 4 '?' characters, prepare for long computation time.
    examples = ["???", "a?a", "kayak", "dojo", "bambi", "?trer??", "?s?dA?dAsd?"]
    for example in examples:
        print(f"{example}:\t{len(replace_question_marks(example))}")


if __name__ == "__main__":
    main()