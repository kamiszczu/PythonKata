"""
PASSED:
https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
"""

def two_oldest_ages(ages):
    return sorted(ages)[-2:]
two_oldest_ages([1, 5, 87, 45, 8, 8])