'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        vex = [[0] * k for k in range(1, 101)]
        vex[0][0] = poured
        flow = 0.0
        for i in range(query_row):
            if all(g < 1 for g in vex[i]):
                return 0
            for j in range(i + 1):
                flow = (vex[i][j] - 1) / 2
                if flow > 0:
                    vex[i + 1][j] += flow
                    vex[i + 1][j + 1] += flow

        return min(1, vex[query_row][query_glass])

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        vex = [[poured]]
        for i in range(query_row):
            if all(g < 1 for g in vex[i]):
                return 0
            vex.append([0] * (i + 2))
            for j in range(i + 1):
                flow = (vex[i][j] - 1) / 2
                if flow > 0:
                    vex[i + 1][j] += flow
                    vex[i + 1][j + 1] += flow

        return min(1, vex[query_row][query_glass])
'''


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        vex = [poured]
        for i in range(query_row):
            if all(g < 1 for g in vex):
                return 0
            newvex = [0] * (i + 2)
            for j in range(i + 1):
                flow = (vex[j] - 1) / 2
                if flow > 0:
                    newvex[j] += flow
                    newvex[j + 1] += flow
            vex = newvex

        return min(1, vex[query_glass])
