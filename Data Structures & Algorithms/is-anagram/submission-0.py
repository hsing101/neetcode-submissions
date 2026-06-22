class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[]
        for c in s:
            l.append(c)
        for d in t:
            if (d not in l):
                return False
            l.remove(d)
        if len(l)==0:
            return True
        return False
        