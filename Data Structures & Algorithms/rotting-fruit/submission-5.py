class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbours = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        ans = 0

        q = deque()
        layer = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    layer.append((r, c))
        q.append(layer)

        def bfs(queue):
            time = 0
            while queue:
                layer = queue.popleft()
                next_layer = []
                for r, c in layer:
                    for dr, dc in neighbours:
                        if r + dr in range(rows) and c + dc in range(cols) and grid[r + dr][c + dc] == 1:
                            grid[r + dr][c + dc] = 2
                            next_layer.append((r + dr, c + dc))
                if next_layer:
                    queue.append(next_layer)
                    time += 1
            return time
        
        ans = bfs(q)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return ans
                    


        
        