import pathlib
import sys

import pytest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from leetcode_algorithms import (
    two_sum,
    valid_parentheses,
    max_sub_array,
    plus_one,
    climb_stairs,
    binary_search,
    majority_element,
    is_anagram,
    pascal_triangle,
    max_profit,
    valid_palindrome,
)


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_valid_parentheses():
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")


def test_max_sub_array():
    assert max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6


def test_plus_one():
    assert plus_one([1, 2, 3]) == [1, 2, 4]


def test_climb_stairs():
    assert climb_stairs(5) == 8


def test_binary_search():
    assert binary_search([1,2,3,4,5], 4) == 3
    assert binary_search([1,2,3,4,5], 6) == -1


def test_majority_element():
    assert majority_element([2,2,1,1,1,2,2]) == 2


def test_is_anagram():
    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")


def test_pascal_triangle():
    assert pascal_triangle(5)[-1] == [1,4,6,4,1]


def test_max_profit():
    assert max_profit([7,1,5,3,6,4]) == 5


def test_valid_palindrome():
    assert valid_palindrome("A man, a plan, a canal: Panama")
    assert not valid_palindrome("race a car")
