from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return False
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, visited, i, j)
                    count += 1
        return count

    def bfs(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int):
        rows, cols = len(grid), len(grid[0])
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1' and not visited[x][y]:
                visited[x][y] = True
                for dx, dy in [(-1, 0), (1 , 0), (0, -1), (0, 1)]:
                    queue.append((x + dx, y + dy))
