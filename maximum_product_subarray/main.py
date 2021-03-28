"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to maximum product subarray
"""

from typing import List
from common.print_functions import print_result


class Solution:
    """
    Given an integer array nums, find a contiguous non-empty subarray
    within the array that has the largest product, and return the product.
    It is guaranteed that the answer will fit in a 32-bit integer.
    A subarray is a contiguous subsequence of the array.

    Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    """
    @staticmethod
    def max_subarray(nums: List[int]) -> int:
        current_min = nums[0]
        current_max = nums[0]
        result = current_max

        for index in range(1, len(nums)):
            current = nums[index]
            new_max = max(current, current_max * current, current_min * current)
            current_min = min(current, current_max * current, current_min * current)

            current_max = new_max
            result = max(result, current_max)

        return result


if __name__ == '__main__':
    solution = Solution()
    dyn_programing = solution.max_subarray([2, 3, -2, 4])
    print_result("Dynamic programing", dyn_programing)
