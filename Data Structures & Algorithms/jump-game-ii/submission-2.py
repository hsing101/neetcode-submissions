class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            ans = float('inf')
            for j in range(1, 1 + nums[i]):
                ans = min(ans, 1 + dfs(i + j))
                memo[i] = ans
            return ans
        return dfs(0)
        