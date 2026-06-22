class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        def backtrack(i):
            if i >= len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            backtrack(i + 1)
            temp.pop()
            backtrack(i + 1)
        backtrack(0)
        return ans

                

                
                


        