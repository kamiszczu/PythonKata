"""
PASSED:
https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce/python
"""


def check(a, limit):
    if limit in a:
        return True
    else:
        return False


"""
another solution
"""

# check=lambda a,x:x in a

# def check(a, x): 
#     return True if x in a else False

# def check(a, x): 
#     return a.__contains__(x)
