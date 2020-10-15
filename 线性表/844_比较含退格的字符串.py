class Solution:
    def getstring(self, s: str) -> str:
        out = []
        for char in s:
            if char != '#':
                out.append(char)
            elif out:
                out.pop()
        return ''.join(out)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getstring(S) == self.getstring(T)
