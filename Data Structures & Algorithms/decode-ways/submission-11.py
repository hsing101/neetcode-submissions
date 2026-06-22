class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s) : 1}
        def dfs(i):
            if i in memo:
                return memo[i]
        
            if s[i] == "0":
                return 0

            count = dfs(i + 1)
            
            if i + 1 < len(s):
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    count += dfs(i + 2)
            memo[i] = count
            return count
        return dfs(0)
            
        
