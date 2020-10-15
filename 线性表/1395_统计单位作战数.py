class Solution:
    ''' 暴搜
    def numTeams(self, rating: list) -> int:
        n = len(rating)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans
    '''
    # 遍历中间点

    def numTeams(self, rating: list) -> int:
        n = len(rating)
        ans = 0

        for j in range(1, n - 1):
            iless = imore = kless = kmore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    iless += 1
                elif rating[i] > rating[j]:
                    imore += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    kless += 1
                elif rating[k] > rating[j]:
                    kmore += 1
            ans += iless * kmore + imore * kless
        return ans
