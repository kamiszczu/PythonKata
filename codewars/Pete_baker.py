"""
PASSED:
https://www.codewars.com/kata/525c65e51bf619685c000059/solutions/python
"""


def cakes(recipe, available):
    tmp_result = []
    for k, v in recipe.items():
        if k in available:
            if available[k] >= recipe[k]:
                tmp_result.append(int(available[k] / recipe[k]))
            elif available[k] < recipe[k]:
                return 0
        else:
            return 0
    return min(tmp_result)


"""
another solution
"""

# def cakes(recipe, available):
#   return min(available.get(ingredient, 0) // quantity for ingredient, quantity in recipe.iteritems())

# def cakes(recipe, available):
#     return min(available.get(ingridient, 0)//amount for ingridient, amount in recipe.items())

# def cakes(recipe, available):
#     ''' Take each ingredient from the recipe, see if it is in the available ones
#         and calculate how many full cakes you can make with it.
#         If an ingredient is missing, we can't bake a cake. Otherwise we have to
#         find the lowest possible amount of cakes.'''
#     return min([available[i]//recipe[i] if i in available else 0 for i in recipe])

# def cakes(recipe, available):
#     return min(available.get(k, 0) // v for k,v in recipe.iteritems())

# def cakes(recipe, available):
#     return min(available.get(k, 0) / recipe[k] for k in recipe)

# def cakes(recipe, available):
#     if set(recipe.keys()).issubset(available.keys()):
#         return min([available[ingredient] / recipe[ingredient]
#                 for ingredient in recipe.keys()])
#     return 0
