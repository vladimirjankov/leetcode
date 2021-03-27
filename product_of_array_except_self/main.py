"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to product of array except self
"""

from typing import List
from common.print_functions import print_result


class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the
    product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    """
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        result = [0] * len(nums)
        for index in range(1, len(nums)):
            left.append(nums[index - 1] * left[index - 1])

        for index in range(len(nums) - 2, -1, -1):
            right[index] = right[index + 1] * nums[index + 1]

        for index in range(0, len(left)):
            result[index] = left[index] * right[index]
        return result

    @staticmethod
    def product_except_self_first_ball(nums: List[int]) -> List[int]:
        product = 1
        number_of_zeros = 0
        last_zero_index = -1
        for index, num in enumerate(nums):
            if num != 0:
                product *= num
            else:
                number_of_zeros += 1
                last_zero_index = index

        if number_of_zeros > 1:
            return [0] * len(nums)
        elif number_of_zeros == 1:
            return_array = [0] * len(nums)
            return_array[last_zero_index] = product
            return return_array
        else:
            return [int(product / value) for value in nums]


if __name__ == '__main__':
    solution = Solution()
    first_ball_solution = solution.product_except_self([4, 5, 1, 8, 2])
    print_result("First ball solution", first_ball_solution)
    first_ball_solution = solution.product_except_self([4, 5, 1, 8, 2])
    print_result("First ball solution", first_ball_solution)
