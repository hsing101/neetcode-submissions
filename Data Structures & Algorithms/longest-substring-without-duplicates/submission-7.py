class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,1
        soln=deque()
        if len(s)==0:
            return 0
        soln+=s[i]
        length=1
        while j<len(s):
            if s[j] not in soln:
                soln+=s[j]
                j+=1
                length=max(length,len(soln))
            else:
                soln.popleft()
        return length




