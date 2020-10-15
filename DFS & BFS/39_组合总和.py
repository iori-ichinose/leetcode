from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        combination = list()

        def dfs(target: int, index: int):
            if index == len(candidates):
                return
            if target == 0:
                if combination not in ans:
                    ans.append(combination[:])

            dfs(target, index + 1)

            if target - candidates[index] >= 0:
                combination.append(candidates[index])
                dfs(target - candidates[index], index)
                combination.pop()

        dfs(target, 0)
        return ans

    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        m = len(candidates)

        def find(s: int, use: List(int), target: int):
            for i in range(s, m):
                num = candidates[i]
                if num == target:
                    ans.append(use + [num])
                elif num < target:
                    find(i, use + [num], target - num)
                else:
                    return

        find(0, [], target)

        return ans
