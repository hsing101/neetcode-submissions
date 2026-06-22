class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        ans = []
        def bfs(r, c):
            pacific, atlantic = False, False
            if r == 0 or c == 0:
                pacific = True
            if r == rows - 1 or c == cols - 1:
                atlantic = True
            if pacific and atlantic:
                return True 
            visited = [(r,c)]
            queue = deque()
            queue.append((r,c))
            neighbors = [[-1,0],[0,-1],[1,0],[0,1]]
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    if (r+dr, c+dc) not in visited and r+dr in range(rows) and c+dc in range(cols):
                        if heights[r+dr][c+dc] <= heights[r][c]: 
                            visited.append((r+dr, c+dc))
                            queue.append((r+dr,c+dc))
                            if r+dr == 0 or c+dc == 0:
                               pacific = True
                            if r+dr == rows - 1 or c+dc == cols - 1:
                               atlantic = True
                            if pacific and atlantic:
                               return True           
            return False
        
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    ans.append([r,c])
        return ans


