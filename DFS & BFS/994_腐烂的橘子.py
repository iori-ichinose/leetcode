from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rol, col = len(grid), len(grid[0])
        fresh = {(i, j) for i in range(rol)
                 for j in range(col) if grid[i][j] == 1}
        rotten = {(i, j) for i in range(rol)
                  for j in range(col) if grid[i][j] == 2}
        time = 0
        direct = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        while fresh:
            if not rotten:
                return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di,
                      dj in direct if (i + di, j + dj) in fresh}
            fresh -= rotten
            time += 1

        return time

    def orangesRotting_bfs(self, grid: List[List[int]]) -> int:
        direct = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        row, col, time = len(grid), len(grid[0]), 0
        queue = [(i, j, 0) for i in range(row)
                 for j in range(col) if grid[i][j] == 2]
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in direct:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))

        for row in grid:
            if 1 in row:
                return -1

        return time
