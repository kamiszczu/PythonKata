"""
PASSED:
https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/python
"""


def countBits(n):
    bits = []
    while (n != 0):
        if n % 2 == 1: bits.append(1)
        n = n // 2
    return len(bits)


"""
another solution
"""

# def countBits(n):
#     return bin(n).count("1")

# def countBits(n):
#     """ count_bits == PEP8, forced camelCase by CodeWars """
#     return '{:b}'.format(n).count('1')

# def countBits(n):
#   return (n & 1) + countBits(n >> 1) if n else 0

# countBits = lambda n: bin(n).count('1')
