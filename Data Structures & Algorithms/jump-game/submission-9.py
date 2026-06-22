class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        count = 1
        while i - count >= 0:
            if count <= nums[i - count]:
                i = i - count
                count = 1
                if i == 0:
                    return True
                continue
            count += 1
        return i == 0
            