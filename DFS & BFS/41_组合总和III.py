from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(cur: int, remain: int, sol: int):
            if remain == 0 and len(sol) == k:
                ans.append(sol[:])
                return
            if cur == 10 or remain < 0 or len(sol) > k:
                return

            dfs(cur + 1, remain - cur, sol + [cur])
            dfs(cur + 1, remain, sol)

        dfs(1, n, [])
        return ans
