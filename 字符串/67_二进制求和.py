class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        ans = []

        length = max(len(a), len(b))
        carry = 0
        for i in range(length):
            carry += 1 if i < len(a) and a[i] == '1' else 0
            carry += 1 if i < len(b) and b[i] == '1' else 0
            ans.append('1' if carry % 2 else '0')
            carry //= 2

        if carry:
            ans.append('1')

        return ''.join(ans[::-1])


s = Solution()
print(s.addBinary('1011', '1010'))
