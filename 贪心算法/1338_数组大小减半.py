from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        sort = sorted(counts.values(), reverse=True)
        cnt, lim, res = 0, len(arr), 0
        for num in sort:
            cnt += num
            res += 1
            if cnt >= lim // 2:
                return res

        return -1
