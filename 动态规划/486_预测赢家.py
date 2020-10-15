from typing import List


class Solution:
    # 递归
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def help(start, end):
            if start == end:
                return nums[start]
            chooseleft = nums[start] - help(start + 1, end)
            chooseright = nums[end] - help(start, end - 1)
            return max(chooseleft, chooseright)

        return help(0, len(nums) - 1) >= 0

    # 动态规划
    def PredictTheWinner_dp(self, nums: List[int]) -> bool:
        if not len(nums) % 2:
            return True
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(length - 2, -1, step=-1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0
