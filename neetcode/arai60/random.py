from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        max_num = 0

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    current_size = self.dfs(grid, visited, i, j)
                    max_num = max(current_size, max_num)
        return max_num
    
    def dfs(self, grid, visted, i, j):
        rows, cols = len(grid), len(grid[0])
        current_size = 0
        stack = [(i, j)]

        while stack:
            x, y = stack.pop()
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1 and not visted[x][y]:
                visted[x][y] = True
                current_size += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((x + dx, y + dy))
        return current_size
