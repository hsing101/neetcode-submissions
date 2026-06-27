class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        def dfs(i, target):
            if i == len(nums):
                return target == 0
            if (i, target) in memo:
                return memo[(i, target)]
            if target < 0:
                return False
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        
        return dfs(0, sum(nums) // 2)
    
            
            
