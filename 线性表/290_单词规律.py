class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        stringArray = s.split(' ')
        words = {}
        i, j = len(pattern), len(stringArray)
        if i != j or i == 0 or j == 0:
            return False

        for i in range(i):
            if pattern[i] in words:
                if words[pattern[i]] != stringArray[i]:
                    return False
            else:
                if stringArray[i] in words.keys():
                    return False
                else:
                    words[pattern[i]] = stringArray[i]
        return True
