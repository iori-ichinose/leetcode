from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = dict()

        for row in matrix:
            if row[0] == 1:
                tup_row = tuple(1 - x for x in row)
            else:
                tup_row = tuple(row)

            if tup_row in d:
                d[tup_row] += 1
            else:
                d[tup_row] = 1

        return max(d.values())
