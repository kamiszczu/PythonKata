def str_count(string, letter):
    return len([i for i in list(string) if i == letter])





"""
another solution
"""

# str_count = lambda strng, letter: strng.count(letter)

def str_count(strng, letter):
    return (strng.count(letter))