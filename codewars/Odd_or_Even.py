"""
PASSED:
https://www.codewars.com/kata/5949481f86420f59480000e7/solutions/python
"""


def odd_or_even(arr):
    number = 0
    for i in arr:
        number += i
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


"""
another solution
"""

# def oddOrEven(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'

# def oddOrEven(arr):
#     return ('even', 'odd')[sum(arr) % 2]
