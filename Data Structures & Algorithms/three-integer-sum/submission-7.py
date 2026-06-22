class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln=[]
        nums.sort()
        for i in range(len(nums)):
            triplet=[]
            target=-nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==target:
                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(nums[k])
                    if triplet not in soln:
                        soln.append(triplet)
                    triplet=[]
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>target:
                    k-=1
                else:
                    j+=1
        return soln