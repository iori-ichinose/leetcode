# https://leetcode-cn.com/problems/implement-rand10-using-rand7/
# The rand7() API is already defined for you.
import random


def rand7():
    return random.randint(1, 7)
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self) -> int:
        a, b = rand7(), rand7()
        while a == 7:
            # 确保a为奇数和偶数的概率相同
            a = rand7()
        while b > 5:
            # 确保b取1-5的概率相同
            b = rand7()

        # 每个数的概率：1/2 * 1/5 = 1/10
        return b + (5 if a & 1 else 0)
