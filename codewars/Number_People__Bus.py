"""
PASSED:
https://www.codewars.com/kata/5648b12ce68d9daa6b000099/solutions/python
"""


def number(bus_stops):
    get_in = [i[0] for i in bus_stops]
    get_of = [i[1] for i in bus_stops]
    # print(sum(get_in) - sum(get_of))
    return sum(get_in) - sum(get_of)


"""
another solution
"""

# def number(bus_stops):
#     return sum([stop[0] - stop[1] for stop in bus_stops])

# def number(stops):
#     return sum(i - o for i, o in stops)

# def number(bus_stops):
#     num = zip(*bus_stops)
#     return sum(num[0])-sum(num[1])

# def number(bus_stops):
#     print(sum(x - y for x,y in bus_stops))
#     return sum(x - y for x,y in bus_stops)

# import operator
# def number(bus_stops):
#     return operator.sub(*map(sum, zip(*bus_stops)))

# def number(bus_stops):
#     return sum(x[0]-x[1] for x in bus_stops)

number([[10, 0], [3, 5], [5, 8]])
