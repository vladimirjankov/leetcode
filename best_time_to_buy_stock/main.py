"""
@author: Vladimir Jankov
@email: vladimir.jankov@outlook.com
@file: main.py
@description: solution to best time to but stock
"""

from typing import List
from common.print_functions import print_result
import sys


class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different
    day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

    Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
    """
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit_value = 0
        for stock in prices:
            if min_price > stock:
                min_price = stock
            elif stock - min_price > max_profit_value:
                max_profit_value = stock - min_price
        return max_profit_value

    @staticmethod
    def max_profit_with_tracking(prices: List[int]) -> int:
        minimum = None
        maximum = None
        start_end = {}
        for index, stock_value in enumerate(prices):
            if minimum is None or minimum > stock_value:
                start_end[stock_value] = stock_value
                minimum = stock_value
                maximum = stock_value
            elif maximum is None or stock_value > maximum:
                start_end = Solution.update(start_end, stock_value)
                maximum = stock_value
        maximum_profit = max([value - key for key, value in start_end.items()])
        return maximum_profit

    @staticmethod
    def update(stock_list, value):
        for key in stock_list.keys():
            if stock_list[key] < value:
                stock_list[key] = value
        return stock_list


if __name__ == '__main__':
    solution = Solution()
    stock_prices = [7, 1, 5, 3, 6, 4]
    max_profit = Solution.max_profit_with_tracking(stock_prices)
    print_result("One pass solution with tracking of peeks", max_profit)
    max_profit = Solution.max_profit(stock_prices)
    print_result("One pass", max_profit)