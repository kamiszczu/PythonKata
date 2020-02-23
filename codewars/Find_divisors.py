"""
PASSED:
https://www.codewars.com/kata/544aed4c4a30184e960010f4/solutions/python
"""


def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)

    if len(result) > 0:
        return result
    else:
        return str(integer) + " is prime"


"""
another solution
"""

# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l

# def divisors(n):
#     return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n

# def divisors(integer):
#   return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

# def divisors(integer):
#   divisors = filter(lambda x: integer % x == 0, range(2, integer // 2 + 1))
#   return divisors if divisors else "{0} is prime".format(integer)

# def divisors(i):
#     y = [x for x in range(2, i/2+1) if i%x==0]
#     return y if y else "{} is prime".format(i)

# def divisors(integer):
#     L = [ n for n in range(2,integer) if not integer % n ]
#     return L if L else "%d is prime" % integer
