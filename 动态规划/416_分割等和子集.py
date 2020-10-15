from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]
