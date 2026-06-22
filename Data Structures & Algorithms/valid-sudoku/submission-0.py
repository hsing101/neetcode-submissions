class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums=[]
        for row in board:
            for c in row:
                if c!=".":
                    nums.append(c)
            if len(nums)!=len(set(nums)):
                return False
            nums=[]
        
        for i in range(9):
            for row in board:
                if row[i]!=".":
                    nums.append(row[i])
            if len(nums)!=len(set(nums)):
                return False
            nums=[]
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if board[i][j]!=".":
                    nums.append(board[i][j])
                if board[i][j+1]!=".":
                    nums.append(board[i][j+1])
                if board[i][j+2]!=".":
                    nums.append(board[i][j+2])
                if board[i+1][j]!=".":
                    nums.append(board[i+1][j])
                if board[i+1][j+1]!=".":
                    nums.append(board[i+1][j+1])
                if board[i+1][j+2]!=".":
                    nums.append(board[i+1][j+2])
                if board[i+2][j]!=".":
                    nums.append(board[i+2][j])
                if board[i+2][j+1]!=".":
                    nums.append(board[i+2][j+1])
                if board[i+2][j+2]!=".":
                    nums.append(board[i+2][j+2])
                if len(nums)!=len(set(nums)):
                    return False
                nums=[]
        return True
            




                


                
            


        