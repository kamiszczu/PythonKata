"""
PASSED:
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/solutions/python
"""


def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m


"""
another solution
"""

# paperwork = lambda m,n: m*n if m>0 and n>0 else 0

# def paperwork(n, m):
#     return max(n, 0)*max(m, 0)
