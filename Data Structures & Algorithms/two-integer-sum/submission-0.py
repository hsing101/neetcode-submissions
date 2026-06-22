class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,1
        l=[]
        num1=nums[i]
        while i<len(nums)-1:
            diff=target-nums[i]
            for j in range(i+1,len(nums)):
                if diff==nums[j]:
                    l.append(i)
                    l.append(j)
                    return l
            i+=1
                
                

            




        