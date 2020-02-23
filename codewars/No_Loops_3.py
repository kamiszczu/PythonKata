def copy(array, start, stop, place):
    cut_aray = array[start:stop]
    my_list = list(array)
    del my_list[place:len(cut_aray) + place]
    my_list.insert(place, cut_aray)
    print(my_list)


copy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 8, 2)

"""
another solution
"""

# def copy(lst, start, stop, place):
#     if stop <= start: return lst
#     array = lst[:]
#     if place < 0: place += len(array)
#     array[place: place + stop - start] = array[start: stop]
#     return array

# def copy(array, start, stop, place):
#     if place < 0:
#         place += len(array)
#     if start < 0:
#         start += len(array)
#     if stop < 0:
#         stop += len(array)
#     if start < stop:
#         array[place : place+(stop-start)] = array[start : stop]
#     return array

# def copy(array, start, stop, place):
#     if place<0: place += len(array)
#     if stop>start: array[place:place+stop-start] = array[start:stop]
#     return array

# def copy(array, start, stop, place):
#     copy = list(map(lambda i: array[i], range(start, stop)))
#     place = (len(array) + place) % len(array)
#     result = array[:place] + copy + array[place+len(copy):]
#     return result
