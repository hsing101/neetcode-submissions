class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        cursum = 0
        if len(nums) == 1:
            return nums[0]
        for r in range(len(nums)):
            cursum += nums[r]
            maxsum = max(maxsum, cursum)
            if cursum < 0:
                cursum = 0
                
        return maxsum
        