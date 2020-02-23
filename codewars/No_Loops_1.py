def check(a, limit):
    if sum(a) <= limit:
        return True
    else:
        return False


check([1, 2, 3], 10)

"""
1_
"""


def check(a, x):
    return x in set(a)


"""
2_
"""


def check(a, x):
    return a.__contains__(x)


"""
3_
"""
check = lambda a, x: True if x in a else False
