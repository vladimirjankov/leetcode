"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to two sums problem
"""

from typing import List
from common.print_functions import print_result


class Solution:
    @staticmethod
    def two_sum_dict_solution(nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return index, num_map[difference]
            num_map[num] = index
        return []

    @staticmethod
    def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
        for index_1, value_1 in enumerate(nums):
            for index_2, value_2 in enumerate(nums):
                if index_1 != index_2:
                    if value_1 + value_2 == target:
                        return index_1, index_2
        return []


if __name__ == '__main__':
    solution = Solution()
    indexes_brute_force = solution.two_sum_brute_force([1, 2, 3], 5)
    print_result("Brute force", indexes_brute_force)
    indexes_dict_solution = solution.two_sum_dict_solution([1, 2, 3], 5)
    print_result("Dictionary solution", indexes_dict_solution)
