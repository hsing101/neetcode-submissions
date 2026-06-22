class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(s):
            if len(s) == 0:
                return 1
            
            if s[0] == '0':
                return 0

            if s[1:] in memo:
                res = memo[s[1:]]
            else:
                 res = dfs(s[1:])
                 memo[s[1:]] = res
            
            if len(s) >= 2 and (s[:2] <= "26"):
                if s[2:] in memo:
                    res += memo[s[2:]]
                else:
                    res += dfs(s[2:])
                    memo[s[2:]] = res
            
            return res
        
        return dfs(s)
