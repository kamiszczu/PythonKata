"""
PASSED:
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/solutions/python
"""


def is_uppercase(inp):
    for i in inp.split():
        if i.isupper() == True:
            return True
        elif i.isupper() == False:
            return False
        else:
            return True


"""
another solution
"""

# def is_uppercase(inp):
#     return not len(set(inp).intersection(set('abcdefghijklmnopqrstuvwxyz')))

# is_uppercase = lambda x: any(97<=ord(i)<=122 for i in x) == False

# is_uppercase = lambda inp: inp.isupper()

# def is_uppercase(inp):
#     return inp.isupper()
