def const(char):
    return char.isalpha() and char not in "aeiou"

def solve(s):
    highv = 0
    current_value = 0

    for char in s:
        if const(char):
            current_value += ord(char) - ord('a') + 1
        else:
            highv = max(highv, current_value)
            current_value = 0
    
    highv = max(highv, current_value)
    return highv
