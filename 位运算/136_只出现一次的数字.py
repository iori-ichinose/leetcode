from typing import List

'''
原题：https://leetcode-cn.com/problems/single-number
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
    1. 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 利用异或，0 ^ n = n, n ^ n = 0，且异或满足交换律：a ^ b ^ c = a ^ c ^ b
        # nums中出去res都出现了两次，则我们引入一个变量res与数组中元素不断异或，根据交换律
        # 所有出现两次的元素异或两次相互抵消，于是剩下的元素就是我们需要求的。
        res = 0
        for num in nums:
            res ^= num

        return res
