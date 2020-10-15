# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。
# 对于一个列表，n-1的数加1实际效果等同于剩下那个数减1，因此最后的情况应该是所有的数减到了最小的那个数，因此把列表中每一个数减去最小的数再求和就是最终移动次数。

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n, ans = min(nums), 0
        for num in nums:
            ans += num - n

        return ans
