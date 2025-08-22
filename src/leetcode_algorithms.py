"""Collection of algorithm implementations inspired by LeetCode problems."""
from __future__ import annotations

from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers such that they add up to ``target``."""
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []


def reverse_integer(x: int) -> int:
    """Reverse digits of a 32-bit signed integer."""
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_x = int(str(x_abs)[::-1])
    reversed_x *= sign
    if -2 ** 31 <= reversed_x <= 2 ** 31 - 1:
        return reversed_x
    return 0


def is_palindrome_number(x: int) -> bool:
    """Check whether ``x`` is a palindrome integer."""
    return str(x) == str(x)[::-1]


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral to an integer."""
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total


def longest_common_prefix(strs: List[str]) -> str:
    """Find the longest common prefix among ``strs``."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix) and prefix:
            prefix = prefix[:-1]
    return prefix


def valid_parentheses(s: str) -> bool:
    """Return True if ``s`` contains valid parentheses."""
    stack: List[str] = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack


def merge_two_lists(l1: List[int], l2: List[int]) -> List[int]:
    """Merge two sorted lists ``l1`` and ``l2`` into a single sorted list."""
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result


def remove_duplicates(nums: List[int]) -> int:
    """Remove duplicates from sorted list ``nums`` in-place and return new length."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def remove_element(nums: List[int], val: int) -> int:
    """Remove all instances of ``val`` in ``nums`` and return new length."""
    write = 0
    for num in nums:
        if num != val:
            nums[write] = num
            write += 1
    return write


def str_str(haystack: str, needle: str) -> int:
    """Return the index of the first occurrence of ``needle`` in ``haystack``."""
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


def search_insert(nums: List[int], target: int) -> int:
    """Find the index to insert ``target`` in the sorted list ``nums``."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def max_sub_array(nums: List[int]) -> int:
    """Return the largest sum of a contiguous subarray."""
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def length_of_last_word(s: str) -> int:
    """Return the length of the last word in ``s``."""
    return len(s.rstrip().split(" ")[-1]) if s.strip() else 0


def plus_one(digits: List[int]) -> List[int]:
    """Increment the integer represented by ``digits`` by one."""
    for i in reversed(range(len(digits))):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def add_binary(a: str, b: str) -> str:
    """Add two binary strings and return the result as a binary string."""
    i, j, carry = len(a) - 1, len(b) - 1, 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        carry, digit = divmod(total, 2)
        result.append(str(digit))
    return ''.join(reversed(result))


def sqrtx(x: int) -> int:
    """Compute the integer square root of ``x``."""
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def climb_stairs(n: int) -> int:
    """Count distinct ways to climb ``n`` stairs taking 1 or 2 steps."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Merge ``nums2`` into ``nums1`` sorted in-place."""
    i, j, write = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1


def binary_search(nums: List[int], target: int) -> int:
    """Classic binary search returning index of ``target`` or -1."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def is_anagram(s: str, t: str) -> bool:
    """Return True if ``t`` is an anagram of ``s``."""
    from collections import Counter

    return Counter(s) == Counter(t)


def majority_element(nums: List[int]) -> int:
    """Return the majority element appearing more than n/2 times."""
    count = candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


def pascal_triangle(num_rows: int) -> List[List[int]]:
    """Generate Pascal's triangle up to ``num_rows`` rows."""
    triangle: List[List[int]] = []
    for row in range(num_rows):
        if row == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            triangle.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
    return triangle


def max_profit(prices: List[int]) -> int:
    """Return the maximum profit from a single stock trade."""
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


def valid_palindrome(s: str) -> bool:
    """Check if ``s`` is a palindrome considering only alphanumerics."""
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]

