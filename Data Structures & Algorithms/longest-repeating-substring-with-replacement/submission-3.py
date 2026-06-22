class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ans = 0
        freq = collections.defaultdict(int)
        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
