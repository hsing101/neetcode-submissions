class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        array = [[] for i in range(len(nums)+1)]
        for num in nums:
            mapp[num] = 1 + mapp.get(num,0)
        for num,count in mapp.items():
            array[count].append(num)
        
        res =[]
        for i in range(len(array)-1,0,-1):
            for num in array[i]:
                res.append(num)
                if len(res) == k:
                    return res
