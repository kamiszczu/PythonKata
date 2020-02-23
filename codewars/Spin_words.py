"""
PASSED:
https://www.codewars.com/kata/5264d2b162488dc400000001/solutions/python
"""


def spin_words(sentence):
    result = ""
    if len(sentence.split(" ")) > 1:
        for k in sentence.split():
            if len(k) >= 5:
                tmp_sentence = [i for i in k]
                tmp_sentence.reverse()
                for j in tmp_sentence: result += j
                result += ' '

            else:
                result += k
                result += ' '

        if result[-1:] == " ":
            result = result[:-1]
        return result
    elif len(sentence) < 5:
        return sentence
    else:
        tmp_sentence = [i for i in sentence]
        tmp_sentence.reverse()
        for j in tmp_sentence: result += j
        return result


"""
another solution
"""

# spin_words = lambda l : ' '.join([(w if len(w)<5 else w[::-1]) for w in l.split(' ')])

# def spin_words(sentence):
#     o=[]
#     l=sentence.split(" ")
#     for i in l:
#         if len(i)>=5:
#             o.append(i[::-1])
#         else:
#             o.append(i)
#     return " ".join(o)

# spin_words=lambda sentence:' '.join((map(lambda e:''.join(reversed(e))if len(e)>=5 else e,sentence.split(' '))))  

# def spin_words(sentence):

#     # If-Else List Comprehension
#     word_list = [word[::-1] if len(word)>=5 else word for word in sentence.split(' ')]  
#     return ' '.join(word_list)

# def spin_words(sentence):
#     spun = []

#     for w in sentence.split():
#         if len(w) >= 5:
#             spun.append(''.join(reversed(w)))
#         else:
#             spun.append(w)

#     return ' '.join(spun)
