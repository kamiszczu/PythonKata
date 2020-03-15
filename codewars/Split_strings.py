"""
PASSED:
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/solutions/python
"""

def solution(s):
    if len(s) % 2 == 0:
        return [s[i:i + 2] for i in range(0, len(s), 2)]
    else:
        result = [s[i:i + 2] for i in range(0, len(s), 2)]
        result_last = result[-1:]
        last_element = result_last[0] + "_"
        del result[-1]
        result.append(last_element)
        return result
    
    
"""
another solution
"""


# def solution(s):
#     if len(s) % 2 == 1:
#         s += '_'
#
#     return [s[i:i + 2] for i in xrange(0, len(s), 2)]

# import re
#
# def solution(s):
#     return re.findall('..', s + '_')

# import re
#
# def solution(s):
#     return re.findall(".{2}", s + "_")

# from itertools import zip_longest
#
# def solution(s):
#     return list("".join(pair) for pair in zip_longest(s[::2], s[1::2], fillvalue="_"))