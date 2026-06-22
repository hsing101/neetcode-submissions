class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * (n + 2)
        for i in range(n - 1, -1 , -1):
            ans[i] = max(nums[i] + ans[i + 2], ans[i + 1])
        return ans[0]
        



        