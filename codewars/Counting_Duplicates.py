"""
PASSED:
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/solutions/python
"""


def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


"""
another solution
"""

# import collections
# def duplicate_count(text):
#     return len(([item for item, count in collections.Counter(list(text)).items() if count > 1]))
