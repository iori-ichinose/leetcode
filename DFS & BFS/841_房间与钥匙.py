class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        visited = list()

        def DFS(n: int):
            visited.append(n)
            for key in rooms[n]:
                if key not in visited:
                    DFS(key)

        return len(visited) == len(rooms)
