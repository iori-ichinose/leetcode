from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        inBlock = False
        res = []
        curLine = []
        for line in source:
            i = 0
            if not inBlock:
                curLine = []
            while i < len(line) - 1:
                if not inBlock and line[i:i + 2] == '/*':
                    inBlock = True
                    i += 2
                elif inBlock and line[i:i + 2] == '*/':
                    inBlock = False
                    i += 2
                elif not inBlock and line[i:i + 2] == '//':
                    break
                elif not inBlock:
                    curLine.append(line[i])
                    i += 1
                else:
                    i += 1
            if i == len(line) - 1 and not inBlock:
                curLine.append(line[-1])
            if curLine and not inBlock:
                res.append(''.join(curLine))
        return res
