class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        now = 0
        res = 0
        for i in croakOfFrogs:
            croak[i] += 1
            if not croak['c'] >= croak['r'] >= croak['o'] >= croak['a'] >= croak['k']:
                return -1
            if i == 'c':
                now += 1
                res = max(now, res)
            elif i == 'k':
                now -= 1

        return res if now == 0 else -1
