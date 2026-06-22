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
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l]!=".":
                            nums.append(board[i+k][j+l])
                if len(nums)!=len(set(nums)):
                    return False
                nums=[]
        return True
            




                


                
            


        