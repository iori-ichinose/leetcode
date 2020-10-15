from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grps = {}
        ans = []
        for index, ID in enumerate(groupSizes):
            if ID not in grps:
                grps[ID] = [index]
            else:
                grps[ID].append(index)

        for l, user in grps.items():
            for i in range(0, len(user), l):
                ans.append(user[i:i + l])

        return ans
