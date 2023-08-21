def const(char):
    return char.isalpha() and char not in "aeiou"

def mysolution(s):
    highestvlue = 0
    myvl = 0

    for char in s:
        if const(char):
            myvl += ord(char) - ord('a') + 1
        else:
            highestvlue = max(highestvlue, myvl)
            myvl = 0
    
    highestvlue = max(highestvlue, myvl)
    return highestvlue
