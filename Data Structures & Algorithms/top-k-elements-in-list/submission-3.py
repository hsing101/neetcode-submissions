class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct=set(nums)
        pairs={}
        soln=[]
        for d in distinct:
            pairs[d]=0

        for num in nums:
            if num in distinct:
                pairs[num]+=1
        freq=list(pairs.values())
        for i in range(k):
            max_val=max(freq)
            for key in pairs.keys():
                if pairs[key]==max_val:
                    soln.append(key)
            freq.remove(max_val)
        return list(set(soln))

