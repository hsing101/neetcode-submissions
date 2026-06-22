class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        chars = list(word)
        

        
        def dfs(r, c, p, board):
           
            neighbours = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            if p == len(chars) - 1:
                nonlocal flag
                flag = True
                return 
            
            for dr, dc in neighbours:
                if r + dr in range(rows) and c + dc in range(cols) and board[r + dr][c + dc] == chars[p + 1] and [r+dr, c+dc] not in visited:
                    visited.append([r+dr, c+dc])
                    dfs(r + dr, c + dc, p + 1, board)
                    visited.pop()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == chars[0]:
                    visited = [[i, j]]
                    flag = False
                    dfs(i, j, 0, board)
                    if flag:
                        return True
        return False
            



        