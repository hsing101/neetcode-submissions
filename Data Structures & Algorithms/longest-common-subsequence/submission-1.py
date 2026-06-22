class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j, ans):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                ans.append(text1[i])
                memo[(i, j)] = 1 + dfs(i + 1, j + 1, ans)
                return 1 + dfs(i + 1, j + 1, ans)
            memo[(i, j)] = max(dfs(i + 1, j, ans), dfs(i, j + 1, ans))
            return max(dfs(i + 1, j, ans), dfs(i, j + 1, ans))

        return dfs(0, 0, [])


        