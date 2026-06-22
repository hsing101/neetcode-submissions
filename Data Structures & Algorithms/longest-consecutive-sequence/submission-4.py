class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        if nums==[]:
            return 0
        
        while len(nums)>0:
            num=nums[0]
            cons=num+1
            des=num-1
            nums.remove(num)
            t_count=1
            d_count=0
            while cons in nums:
                nums.remove(cons)
                t_count+=1
                cons+=1
            while des in nums:
                nums.remove(des)
                d_count+=1
                des-=1
            if t_count+d_count>count:
                count=t_count+d_count
        return count
                

            
        