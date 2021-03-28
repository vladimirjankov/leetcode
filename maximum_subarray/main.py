"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to maximum subarray
"""

from typing import List
from common.print_functions import print_result


class Solution:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.

    Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Example 2:
    Input: nums = [1]
    Output: 1

    Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    """
    @staticmethod
    def max_subarray(nums: List[int]) -> int:
        current_subarray = nums[0]
        max_subarray = current_subarray

        for index in range(1, len(nums)):
            if current_subarray < 0:
                current_subarray = nums[index]
            else:
                current_subarray += nums[index]

            if current_subarray > max_subarray:
                max_subarray = current_subarray

        return max_subarray

    @staticmethod
    def max_subarray_div_and_conq(nums: List[int]) -> int:
        return Solution.best_subarray(nums, 0, len(nums) - 1)

    @staticmethod
    def best_subarray(nums, left, right):
        if left > right:
            return - math.inf

        middle = (left + right) // 2

        current_sum = 0
        left_sum = 0
        right_sum = 0

        for index in range(middle - 1, left - 1, -1):
            current_sum += nums[index]
            left_sum = max(left_sum, current_sum)

        current_sum = 0
        for index in range(middle + 1, right + 1):
            current_sum += nums[index]
            right_sum = max(right_sum, current_sum)

        total_sum = nums[middle] + right_sum + left_sum

        left_half = Solution.best_subarray(nums, left, middle - 1)
        right_half = Solution.best_subarray(nums, middle + 1, right)

        return max(total_sum, left_half, right_half)


if __name__ == '__main__':
    solution = Solution()
    dyn_programing = solution.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print_result("Dynamic programing", dyn_programing)
    div_and_conq_programing = solution.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print_result("Divide and conquer", div_and_conq_programing)

