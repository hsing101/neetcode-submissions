class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        longest = 1
        if len(s) == 0:
            return 0
        while j < len(s):
            length = 1
            sett = set()
            sett.add(s[i])
            while j < len(s) and s[j] not in sett :
                sett.add(s[j])
                length += 1
                longest = max(longest, length)
                j += 1
            i += 1
            j = i + 1
        return longest

            





