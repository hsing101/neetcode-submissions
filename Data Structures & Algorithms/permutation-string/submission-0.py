class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        o_count = {}
        for k in range(len(s1)):
            o_count[s1[k]] = 1 + o_count.get(s1[k],0)
        i, j = 0, len(s1)-1
        while j < len(s2):
            count = {}
            for k in range(i, j+1):
                count[s2[k]] = 1 + count.get(s2[k],0)
            if count == o_count:
                return True
            i += 1
            j += 1
        return False
            


        
        