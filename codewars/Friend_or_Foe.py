"""
PASSED:
https://www.codewars.com/kata/55b42574ff091733d900002f/solutions/python
"""


def friend(x):
    return [i for i in x if len(i) == 4]


"""
another solution
"""

# def friend(x):
#     return list(filter(lambda s : len(s)==4 ,x))
