"""
PASSED:
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/solutions/python
"""


def is_uppercase(inp):
    return not len(set(inp).intersection(set('abcdefghijklmnopqrstuvwxyz')))


def find_uniq(arr):
    for i in arr:
        result = list(filter(lambda x: x == i, arr))
        if len(result) == 1:
            return result[0]


"""
another solution
"""

# def find_uniq(arr):
#     for n in list(set(arr)):
#         if arr.count(n) == 1:
#             return n   # n: unique integer in the array

# def find_uniq(arr):
#     return max(arr) if arr.count(max(arr)) == 1 else min(arr)
