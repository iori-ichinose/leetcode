class Solution:
    # Normal
    def myAtoi(self, s: str) -> int:
        out = []
        s = s.lstrip()
        flag = '+'
        sym = ['+', '-']
        if not s:
            return 0
        if s[0] in sym and len(s) == 1:
            return 0

        if s[0] in sym and len(s) > 1:
            flag = s[0]
            s = s[1:]

        for ch in s:
            if ch.isdigit():
                out.append(ch)
            else:
                break

        if not out:
            return 0
        elif flag == '-':
            return -min(int(''.join(out)), 2147483648)
        else:
            return min(int(''.join(out)), 2147483647)

    # Automation
    class Automation:
        def __init__(self):
            # 0: start
            # 1: signed
            # 2: in_number
            # 3: end
            self.state = 0
            self.sign = 1
            self.ans = 0
            self.table = [
                [0, 1, 2, 3],
                [3, 3, 2, 3],
                [3, 3, 2, 3],
                [3, 3, 3, 3]
            ]

        def get_col(self, c: str):
            if c == ' ':
                return 0
            elif c in ['+', '-']:
                return 1
            elif c.isdigit():
                return 2
            else:
                return 3

        def get(self, c: str):
            self.state = self.table[self.state][self.get_col(c)]

            if self.state == 1:
                self.sign = 1 if c == '+' else -1
            elif self.state == 2:
                self.ans = min(self.ans * 10 + int(c),
                               2147483647 if self.sign == 1 else 2147483648)

    def myAtoi_2(self, s: str) -> int:
        auto = self.Automation()
        for c in s:
            auto.get(c)
        return auto.sign * auto.ans
