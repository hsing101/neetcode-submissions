class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i >= len(s):
                return 1
            
            dig = int(s[i])

            if dig == 0:
                return 0

            count = dfs(i + 1)
            
            if i + 1 < len(s):
                next_dig = int(s[i + 1])
                if dig == 1 or (dig == 2 and next_dig <= 6):
                    count += dfs(i + 2)
            memo[i] = count
            return count
        return dfs(0)
            
        
