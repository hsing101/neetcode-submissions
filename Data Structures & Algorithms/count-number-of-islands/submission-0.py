class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        soln = 0

        def bfs(r, c, grid):
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            queue = deque()
            queue.append([r, c])
            visited.add((r, c))
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    if r + dr in range(rows) and c + dc in range(cols) and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == '1':
                        queue.append([r+dr, c+dc])
                        visited.add((r+dr, c+dc))
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j, grid)
                    soln += 1
        
        return soln
            




        