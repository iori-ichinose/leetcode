from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = 0
        friends = {}
        for i, j in pairs:
            friends[i], friends[j] = j, i

        for x in range(n):
            y = friends[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = friends[u]
                if preferences[u].index(x) < preferences[u].index(v):
                    unhappy += 1
                    break

        return unhappy
