"""
This program shows two solutions of changing roman numerals to arabic.
First one is more clean and straightforward and second one is more manual and more prone to errors while implementing
"""

# Would be easier if keys and values in combinations were swapped, but this also works
combinations = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

def romanToInt(s: str) -> int:
    result = 0
    i = 0
    while i < len(s):
        #[i:i+2], because we are looking for 4,9,40,90,400,900 (in roman) and slices of [i:i] return None, hence +2 meaning of length 2.
        if s[i:i+2] in combinations.values():
            print(s[i:i+2])
            #Turning keys of combinations into a list and then finding a specific index of list of values
            result += list(combinations.keys())[list(combinations.values()).index(s[i:i+2])]
            i += 1
        elif s[i] in combinations.values():
            #Same thing as above but different value to search
            result += list(combinations.keys())[list(combinations.values()).index(s[i])]
        i += 1
    return result

def romanToIntv2(s: str) -> int:
    result = 0
    numerals = [[keys, s.count(values)] for keys, values in combinations.items()]
    """
    This section is responsible for subtracting repeating symbols
    example: string 'IV' counts as [[1, 1], [4, 1], [5, 1],...] 
    What we have to do is subtract the two letter numeral from all single letter numerals.
    result: [[1, 0], [4, 1], [5, 0],...]
    This is quite bad, as below code requires manual counting and indexing to implement correctly.
    """
    numerals[0][1] -= numerals[1][1]
    numerals[0][1] -= numerals[3][1]
    numerals[2][1] -= numerals[1][1]
    numerals[4][1] -= numerals[3][1]
    numerals[4][1] -= numerals[5][1]
    numerals[4][1] -= numerals[7][1]
    numerals[6][1] -= numerals[5][1]
    numerals[8][1] -= numerals[7][1]
    numerals[8][1] -= numerals[9][1]
    numerals[8][1] -= numerals[11][1]
    numerals[10][1] -= numerals[9][1]
    numerals[12][1] -= numerals[11][1]
    for combo in numerals:
        result += combo[0]*combo[1]
    return result

print(romanToInt("MCD"))
