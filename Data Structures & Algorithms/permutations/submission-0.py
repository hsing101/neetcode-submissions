class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            def backtrack(array):
                if len(array) <= 0:
                    return [[]]
                return_val = []
                digit = array[0]
                if len(array) == 1:
                    return_val.append([digit])
                    return return_val
                sub_arrays = backtrack(array[1:])
                for sub_array in sub_arrays:
                    for i in range(len(sub_array) + 1):
                        copy = sub_array[:]
                        copy.insert(i, digit)
                        return_val.append(copy)
                return return_val
            return backtrack(nums)


                
    
                






