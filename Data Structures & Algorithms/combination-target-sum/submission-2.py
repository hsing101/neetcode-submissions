class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        soln, temp = [], [] 
        def backtrack(nums, target, i): 
            for j in range (i, len(nums)): 
                if sum(temp) < target: 
                    temp.append(nums[j]) 
                    backtrack(nums, target, j)
                    temp.pop()
                elif sum(temp) == target: 
                    soln.append(temp[:])
                    return 
                else: 
                    return 
        backtrack(nums, target, 0)
        return soln


