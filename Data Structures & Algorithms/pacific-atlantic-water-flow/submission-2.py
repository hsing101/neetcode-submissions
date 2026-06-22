class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = set()
        atl = set()

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in ocean and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        ocean.add((nr, nc))

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            pac.add((0,c))
            atlantic.append((ROWS - 1, c))
            atl.add((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            pac.add((r,0))
            atlantic.append((r, COLS - 1))
            atl.add((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        return res
        