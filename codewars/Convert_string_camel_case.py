# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    result = ""
    if '-' in text:
        tm = text.split("-")
        for i in tm: result += i
        # print(result)
        return result
    else:
        tm = text.split("_")
        first = tm[0].lower()
        del tm[0]
        for i in tm: result += i.title()

        # print(first+result)
        return first + result


to_camel_case("The-Stealth-Warrior")
to_camel_case("the_stealth_warrior")

# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
