class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # only start counting if it's the first in the sequence
            if n - 1 not in numset:
                length = 1
                curr = n
                while curr + 1 in numset:
                    curr += 1
                    length += 1
                longest = max(longest, length)

        return longest


                

            
        