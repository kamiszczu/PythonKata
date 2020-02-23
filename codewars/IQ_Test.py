"""
PASSED:
https://www.codewars.com/kata/552c028c030765286c00007d/solutions/python
"""


def iq_test(numbers):
    numbers_list = numbers.split(" ")
    numbers_list = list(map(int, numbers_list))
    result_value_pos = 0
    result_value_neg = 0

    counter_positive = counter_negative = 0
    for i in numbers_list:
        if i % 2 == 0:
            counter_positive += 1
            result_value_pos = i
        else:
            counter_negative += 1
            result_value_neg = i

    result = 0
    if counter_positive < counter_negative:
        result = result_value_pos
    else:
        result = result_value_neg

    # print(numbers_list.index(result)+1)
    return numbers_list.index(result) + 1


iq_test("2 2 1 2")

"""
another solution
"""

# def iq_test(numbers):
#     odds = [i for i in numbers.split(" ") if int(i) % 2 != 0]
#     even = [i for i in numbers.split(" ") if int(i) % 2 == 0]
#     ans = [odds,even][len(even)==1][0]
#     return numbers.split(" ").index(ans)+1

# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

# def iq_test(numbers):
#   a=list(map(lambda x : int(x)%2,numbers.split(' ')))
#   return 1+(a.index(0) if (a.count(0)) == 1 else a.index(1))

# iq_test = lambda numbers: (lambda l: l.index(sum(l)==1)+1)([n%2 for n in map(int, numbers.split())])
