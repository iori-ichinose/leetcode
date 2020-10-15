# https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/submissions/
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        in_1 = {rest: index for index, rest in enumerate(list1)}
        in_2 = {rest: index for index, rest in enumerate(list2)}
        if len(list1) < len(list2):
            cross = [rest for rest in in_1 if rest in in_2]
        else:
            cross = [rest for rest in in_2 if rest in in_1]
        sum_index = {rest: in_1[rest] + in_2[rest] for rest in cross}

        m = min(sum_index.values())
        return [key for key, val in sum_index.items() if val == m]
