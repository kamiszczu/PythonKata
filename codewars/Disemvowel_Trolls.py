"""
PASSED:
https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/python
"""


def disemvowel(vowel_negative):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_tmp = list(vowel_negative)
    for i in vowel:
        for k in vowel_tmp:
            if i.lower() == k.lower():
                vowel_tmp.remove(k)

    result = ""
    for j in vowel_tmp:
        result += j

    return result


"""
another solution
"""

# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")

# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")

# import re
# def disemvowel(string):
#     return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s

# import re
# def disemvowel(string):
#     return re.sub(r"[aeiouAEIOU]", "", string)

# def disemvowel(string):
#   return "".join([c for c in string if c not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']])

# def disemvowel(string):
#     v = 'aeiouAEIOU'
#     return filter(lambda x: x not in v, string)
