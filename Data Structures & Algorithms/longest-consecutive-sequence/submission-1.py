class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0

        for num in nums:
            cons=num+1
            t_count=1
            while cons in nums:
                t_count+=1
                cons+=1
            if t_count>count:
                count=t_count
        if nums==[]:
            return 0
        return count
                

            
        