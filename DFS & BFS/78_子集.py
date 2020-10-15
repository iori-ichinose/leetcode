from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        tmp = []

        def dfs(k: int):
            if k == n:
                res.append(tmp[:])
                return
            tmp.append(nums[k])
            dfs(k + 1)
            tmp.pop()
            dfs(k + 1)

        dfs(0)
        return res
