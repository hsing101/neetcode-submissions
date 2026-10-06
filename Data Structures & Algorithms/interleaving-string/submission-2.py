class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i, j, k = 0, 0, 0
        memo = {}
        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i, j)]
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            memo[(i, j)] = False

            if j < len(s2) and s2[j] == s3[k]:
                memo[(i, j)] = dfs(i, j + 1, k + 1)
            if not memo[(i, j)] and i < len(s1) and s1[i] == s3[k]:
                memo[(i, j)] = dfs(i + 1, j, k + 1)
            return memo[(i, j)]



        return dfs(0, 0, 0)
            
            

        