# def square_sums_row(array_n):
#     # if len(array_n) % 2 != 0:
#     #     False
#     # else:        
#     for i in array_n:
#         array_n.remove(i)
#         zip_result = zip([i], array_n)
#         for k in zip_result:
#             print(k)
#             sum_from_number = k[0] + k[1]
#             if sum_from_number**.5%1 == 0:
#                 print("Number is perfect square")
#                 return sum_from_number


square_sums_row = [9]

"""
Sample test
"""


def doTests():
    for i in [15, 23, 25]:
        actual = square_sums_row(i)
        print(i, actual)
        a = actual[:-1]
        b = actual[1:]
        for x in zip(a, b):
            if sum(x) ** .5 % 1:
                test.expect(0, 'sums of adjacent numbers should be squares')
                return
        actual.sort()
        test.assert_equals(actual, list(range(1, i + 1)), 'missing numbers')


doTests()
