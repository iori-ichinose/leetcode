class Solution:
    def calculate(self, s: str) -> int:
        sign = list()
        sign.append(1)
        ans, num, op = 0, 0, 1
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            ans += op * num
            num = 0
            if c == '+':
                op = sign[-1]
            elif c == '-':
                op = -sign[-1]
            elif c == '(':
                sign.append(op)
            else:
                sign.pop()

        ans += op * num
        return ans
