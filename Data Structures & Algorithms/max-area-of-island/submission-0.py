class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        neighbours = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        visited = set()
        max_area = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            area = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbours:
                    if r + dr in range(rows) and c + dc in range(cols) and grid[r + dr][c + dc] == 1 and (r + dr, c + dc) not in visited:
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))
                        area += 1

            return area  
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    new_area = bfs(r, c)
                    max_area = max(max_area, new_area)
        
        return max_area

             