"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to two sums problem
"""

from typing import List
from common.print_functions import print_result


class Solution:
    """
    Given an integer array nums, return true if any value appears at least twice in the
    array, and return false if every element is distinct.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: true

    Example 2:
    Input: nums = [1,2,3,4]
    Output: false

    Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

    """
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        unique_numbers = set()
        for num in nums:
            if num in unique_numbers:
                return True
            else:
                unique_numbers.add(num)
        return False


if __name__ == '__main__':
    solution = Solution()
    boolean_brute_force = solution.contains_duplicate([1, 2, 3, 1])
    print_result("Brute force", boolean_brute_force)
