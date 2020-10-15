from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        res = [0 for _ in range(N)]
        graph = [[] for _ in range(N)]
        sz = [0 for _ in range(N)]
        dp = [0 for _ in range(N)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(u: int, f: int):
            sz[u] = 1
            dp[u] = 0
            for v in graph[u]:
                if v == f:
                    continue

                dfs(v, u)
                dp[u] += dp[v] + sz[v]
                sz[u] += sz[v]

        def dfs2(u: int, f: int):
            res[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue
                ori_dpu, ori_dpv = dp[u], dp[v]
                ori_szu, ori_szv = sz[u], sz[v]

                dp[u] -= dp[v] + sz[v]
                sz[u] -= sz[v]
                dp[v] += dp[u] + sz[u]
                sz[v] += sz[u]

                dfs2(v, u)

                dp[u], dp[v] = ori_dpu, ori_dpv
                sz[u], sz[v] = ori_szu, ori_szv

        dfs(0, -1)
        dfs2(0, -1)
        return res


s = Solution()
print(s.sumOfDistancesInTree(N=6, edges=[
      [0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
