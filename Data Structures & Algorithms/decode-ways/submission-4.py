class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(s):
            if len(s) == 0:
                return 1
            
            if s[0] == '0':
                return 0
            
            if s in memo:
                return memo[s]

            res = dfs(s[1:])
            
            if len(s) >= 2 and (s[:2] <= "26"):
                res += dfs(s[2:])

            memo[s] = res            
            return res
        
        return dfs(s)
