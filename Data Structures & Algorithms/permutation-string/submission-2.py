class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        o_count = {}
        count = {}
        if len(s1) > len(s2):
            return False
        for k in range(len(s1)):
            o_count[s1[k]] = 1 + o_count.get(s1[k],0)
            count[s2[k]] = 1 + count.get(s2[k],0)
        i, j = 0, len(s1)-1
        while j < len(s2):
            if count == o_count:
                return True
            count[s2[i]] = count.get(s2[i]) - 1
            if count[s2[i]] == 0:
                del count[s2[i]]
            i += 1
            j += 1
            if j == len(s2):
                break
            count[s2[j]] = count.get(s2[j],0) + 1            
        return False
            


        
        