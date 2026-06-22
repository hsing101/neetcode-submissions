class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        suffix=[]
        soln=[]
        rev=nums[::-1]
        prod1,prod2=1,1
        prefix.append(prod1)
        suffix.append(prod2)
        for i in range(1,len(nums)+1):
            prod1*=nums[i-1]
            prefix.append(prod1)
            prod2*=rev[i-1]
            suffix.append(prod2)
        for i in range(0,len(nums)):
            soln.append((prefix[i])*(suffix[len(nums)-i-1]))
        return soln
