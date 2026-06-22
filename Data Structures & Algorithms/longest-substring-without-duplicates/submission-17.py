class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        sett = set()
        for j in range(len(s)):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            sett.add(s[j])
            longest = max(longest,  j - i + 1)
        return longest
        

            





