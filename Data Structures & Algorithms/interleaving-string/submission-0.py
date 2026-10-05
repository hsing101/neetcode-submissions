class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i, j, k = 0, 0, 0
        memo = {}
        def dfs(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            if j < len(s2) and s2[j] == s3[k]:
                return dfs(i, j + 1, k + 1)
            if i < len(s1) and s1[i] == s3[k]:
                return dfs(i + 1, j, k + 1)
            return False
        return dfs(0, 0, 0)
            
            

        