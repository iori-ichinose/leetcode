from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rol, col = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < rol and 0 <= ny < col and (nx, ny) not in visited:
                    if dfs(nx, ny, k + 1):
                        visited.remove((i, j))
                        return True

            visited.remove((i, j))
            return False

        for i in range(rol):
            for j in range(col):
                if dfs(i, j, 0):
                    return True

        return False
