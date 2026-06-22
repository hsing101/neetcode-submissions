class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l, r = 0, 0
        ans = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            ans = max(ans, r - l + 1)
        return ans


