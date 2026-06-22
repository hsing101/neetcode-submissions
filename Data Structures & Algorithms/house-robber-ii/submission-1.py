class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[0:len(nums)-1]), self.rob1(nums[1:len(nums)]))
        
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * (n + 2)
        for i in range(n - 1, -1 , -1):
            ans[i] = max(nums[i] + ans[i + 2], ans[i + 1])
        return ans[0]
        
        