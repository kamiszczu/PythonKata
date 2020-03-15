import unittest

from codewars.Angle import angle
from codewars.Beginner_Series_1 import paperwork
from codewars.Bit_Counting import countBits
from codewars.Counting_Duplicates import duplicate_count
from codewars.Disemvowel_Trolls import disemvowel
from codewars.Expressions_Matter import expression_matter
from codewars.Find_divisors import divisors
from codewars.Find_unique_number import find_uniq
from codewars.Friend_or_Foe import friend
from codewars.Human_readable_duration_format import format_duration
from codewars.Is_string_uppercase import is_uppercase
from codewars.Odd_or_Even import odd_or_even
from codewars.Pete_baker import cakes
from codewars.Spin_words import spin_words
from codewars.The_Hashtag_Generator import generate_hashtag
from codewars.Two_oldest_ages import two_oldest_ages


class TestCase(unittest.TestCase):

    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

    def test_divisors(self):
        self.assertEqual(divisors(15), [3, 5])

    def test_frient(self):
        self.assertEqual(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])

    def test_angle(self):
        self.assertEqual(angle(4), 360)

    def test_sping_words(self):
        self.assertEqual(spin_words("to"), "to")

    def test_find_uniq(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)

    def test_cakes(selfs):
        recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
        available = {'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}
        selfs.assertEqual(int(cakes(recipe, available)), 0)

    def test_is_uppercase(self):
        self.assertEqual(is_uppercase("hello I AM DONALD"), False)

    def test_odd_or_even(self):
        self.assertEqual(odd_or_even([0, 1, 2]), "odd")

    def test_paperwork(self):
        self.assertEqual(paperwork(5, 5), 25)

    def test_duplicate_count(self):
        self.assertEqual(duplicate_count("i11ndivisibyility"), 2)

    def test_count_bit(self):
        self.assertEqual(countBits(17), 2)

    def test_generate_hashtaf(self):
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')

    def test_expression_matter(self):
        self.assertEqual(expression_matter(1, 10, 1), 12)

    def test_format_duration(self):
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")

    def test_two_oldest_ages(self):
        self.assert_equals(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])

