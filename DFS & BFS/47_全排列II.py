from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        part = []
        l = len(nums)
        visit = [False] * l

        def dfs(n: int):
            if n == len(nums):
                ans.append(part[:])
                return
            for i in range(l):
                if visit[i] or (i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]):
                    continue

                part.append(nums[i])
                visit[i] = True
                dfs(n + 1)
                visit[i] = False
                part.pop()

        nums.sort()
        dfs(0)
        return ans
