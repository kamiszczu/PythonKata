"""
WRONG:
https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python
"""


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


phil = Student("Phil", 2, 2, 111)
cam = Student("Cameron", 2, 2, 111)
geoff = Student("Geoff", 2, 2, 111)


def most_money(student):
    sums = 0
    dicks = {}
    result = []
    for i in student:
        sums += i.fives
        sums += i.tens
        sums += i.twenties
        dicks[i.name] = sums
        sums = 0
    for k, v in dicks.items():
        result.append(v)

    # for k in result:
    result2 = list(filter(lambda x: x == k, result))
    if len(result2) == len(result):
        # print(len(result2))
        return 'all'
    else:
        result3 = list(filter(lambda x: x == max(result), result))
        return list(dicks.keys())[list(dicks.values()).index(result3[0])]
        # print(list(dicks.keys())[list(dicks.values()).index(result3[0])])


most_money([phil, cam, geoff])
